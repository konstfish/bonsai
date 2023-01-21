import logging
import json
from datetime import datetime

import grpc
import asyncio

import bonsai_pb2
import bonsai_pb2_grpc

from controllers import RethinkServerConnection, rethink

import hashlib

def create_key(host):
    encrypt = host["job"] + host["host"] + str(host["interval"])
    h = hashlib.new('sha256')
    h.update(str.encode(encrypt))

    return str(h.hexdigest())


logger = logging.getLogger('bonsai')    

class BonsaiServer(bonsai_pb2_grpc.BonsaiServiceServicer):
    async def RegisterClient(self, request: bonsai_pb2.RegistrationRequest,
                        context: grpc.aio.ServicerContext) -> bonsai_pb2.RegistrationConfirmation:
        logger.info('Registration request from host %s!' % request.host)
        
        rjson = {
            'job': request.job,
            'host': request.host,
            'interval': request.interval,
            'labels': request.labels,
            'scrapers': request.scrapers,
            'registration_date': str(datetime.now())
        }

        key = create_key(rjson)
        rjson['id'] = key

        with RethinkServerConnection(rethink_server=rethink) as conn:
            out = rethink.r.table("hosts").insert(rjson, conflict="update").run(conn)
            logger.debug(out)

        return bonsai_pb2.RegistrationConfirmation(code=200, exporter_key=key)

    async def PushMetrics(self, request: bonsai_pb2.MetricsRequest,
                        context: grpc.aio.ServicerContext) -> bonsai_pb2.MetricsConfirmation:
        logger.info('Recieved from host %s' % request.exporter_key)
        
        #labels = {}
        #for label in request.labels:
        #    labels[label] = request.labels[label].label
        

        # filter out unregistered hosts
        with RethinkServerConnection(rethink_server=rethink) as conn:
            out = rethink.r.table('hosts').get_field('id').run(conn)

            if(request.exporter_key not in out):
                logger.info('Host %s not registered' % request.exporter_key)
                return bonsai_pb2.MetricsConfirmation(code=401, confirm="not registered")

        rjson = {
            'id': request.exporter_key,
            'metrics': json.loads(request.metrics.decode('utf-8')),
            'date': str(datetime.now())
        }

        with RethinkServerConnection(rethink_server=rethink) as conn:
            out = rethink.r.table("metrics").insert(rjson, conflict="update").run(conn)
            if(out['replaced'] == 1):
                logger.info('Replaced metrics for host %s' % request.exporter_key)
            else:
                logger.info(out)

        return bonsai_pb2.MetricsConfirmation(code=200, confirm="success")

