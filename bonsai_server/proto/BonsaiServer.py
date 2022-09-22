import logging
import json
from datetime import datetime

import grpc
import asyncio

import bonsai_pb2
import bonsai_pb2_grpc

from controllers import RethinkServerConnection, rethink

logger = logging.getLogger('bonsai')

class BonsaiServer(bonsai_pb2_grpc.ServerServicer):
    async def PushMetrics(self, request: bonsai_pb2.MetricsRequest,
                        context: grpc.aio.ServicerContext) -> bonsai_pb2.MetricsConfirmation:
        logger.info('Recieved from host %s!' % request.host)

        rjson = {
            'id': request.id,
            'job': request.job,
            'host': request.host,
            'metrics': json.loads(request.metrics.decode('utf-8')),
            'labels': request.labels,
            'date': str(datetime.now())
        }

        with RethinkServerConnection(rethink_server=rethink) as conn:
            out = rethink.r.table("metrics").insert(rjson, conflict="update").run(conn)
            logger.debug(out)

        return bonsai_pb2.MetricsConfirmation(code=200, confirm="success")

