import logging

def create_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    default_handler = logging.StreamHandler()
    default_handler.setFormatter(
        logging.Formatter("[%(asctime)s] [%(process)d] [%(levelname)s] [%(module)s] %(message)s")
    )
    logger.addHandler(default_handler)

    return logger

logger = create_logger('bonsai')

import socket
import sched
import time

from datetime import datetime

import psutil

import proto
import json
import grpc
from grpc._channel import _InactiveRpcError
import bonsai_pb2
import bonsai_pb2_grpc

# BonsaiClient Class
class BonsaiClient:
    def __init__(self, bonsai_server, jobname="demo", hostname=None, rate=5, labels=[], exporters=[], server_key=None, certfile=None):
        # if no hostname is defined, get system hostname
        if(hostname == None):
            hostname = socket.gethostname()

        self.bonsai_server = bonsai_server
        self.jobname = jobname
        self.hostname = hostname
        self.labels = labels
        self.rate = rate # [s]
        self.server_key = server_key

        self.exporters = exporters
        
        self.credentials = None

        if(certfile):
            certificate_chain = open(certfile, 'rb').read()
            self.credentials = grpc.ssl_channel_credentials(certificate_chain)

        self.key = self.register()
        logger.info("Recieved Key: %s" % self.key)

        # event loop, that runs the scraper every n seconds
        self.event_loop = sched.scheduler(time.time, time.sleep)
        self.run()
        self.event_loop.run()

    def register(self):
        logger.info("Strating Registration process")
        code = 400

        # while registration is unsuccessful
        while(code != 200):
            #print(json.dumps(data).encode('utf-8'))

            exporter_list = []
            for exporter in self.exporters:
                exporter_list.append(exporter.name)
            
            # create registration request protobuf message
            registration_req = bonsai_pb2.RegistrationRequest( 
                                            job=self.jobname, 
                                            host=self.hostname, 
                                            interval=self.rate,
                                            labels=self.labels,
                                            scrapers=exporter_list
                                            )
            if(self.server_key != None):
                registration_req.key = self.server_key
            
            try:
                if(self.credentials):
                    with grpc.secure_channel(self.bonsai_server, self.credentials) as channel:
                        stub = bonsai_pb2_grpc.BonsaiServiceStub(channel)
                        response = stub.RegisterClient(registration_req)
                else:
                    with grpc.insecure_channel(self.bonsai_server) as channel:
                        stub = bonsai_pb2_grpc.BonsaiServiceStub(channel)
                        response = stub.RegisterClient(registration_req)
                code = response.code
            except _InactiveRpcError:
                logger.info("Unable to reach Bonsai Server, trying again in 5 seconds")
                time.sleep(5)
            except Exception as e:
                logger.info("Issue during communication with Bonsai Server, trying again in 5 seconds")
                print(e.message, e.args)
                time.sleep(5)
            else:
                if(code == 401):
                    logger.info("Exporter unauthorized, trying again in 5 seconds")
                    time.sleep(5)
                elif(code != 200):
                    logger.info("Unable to retrieve Registration, trying again in 5 seconds")
                    time.sleep(5)

        return response.exporter_key

    def run(self):
        start_metrics = time.time()
        metrics = self.build_request()
        end_metrics = time.time()

        logger.info("[TIME] Scraping: %fs" % (end_metrics - start_metrics))

        start_channel = time.time()
        try:
            if(self.credentials):
                with grpc.secure_channel(self.bonsai_server, self.credentials) as channel:
                    stub = bonsai_pb2_grpc.BonsaiServiceStub(channel)
                    response = stub.PushMetrics(metrics)
            else:
                with grpc.insecure_channel(self.bonsai_server) as channel:
                    stub = bonsai_pb2_grpc.BonsaiServiceStub(channel)
                    response = stub.PushMetrics(metrics)
        except _InactiveRpcError:
            logger.info("Unable to reach Bonsai Server, trying again in 5 seconds")
            time.sleep(5)
        except Exception as e:
            logger.info("Issue during communication with Bonsai Server, trying again in 5 seconds")
            print(e.message, e.args)
            time.sleep(5)
        else:

            end_channel = time.time()

            logger.info("[TIME] Transfer: %fs" % (end_channel - start_channel))
            logger.info("Recv: %d" % response.code)

            # failsafe, should the database somehow get lost, reregister
            if(response.code == 401):
                self.register()

        self.event_loop.enter(self.rate, 1, self.run)

    def build_request(self):
        data = {}
        for exporter in self.exporters:
            data[exporter.name] = exporter.get_metrics()

        # print(data)        

        #print(json.dumps(data).encode('utf-8'))
        metric_req = bonsai_pb2.MetricsRequest(
                        exporter_key=self.key,
                        metrics=json.dumps(data).encode('utf-8')
                        )

        return metric_req
