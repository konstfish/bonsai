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
from datetime import datetime
import time

import proto
import json
import grpc
import bonsai_pb2
import bonsai_pb2_grpc

class BonsaiClient: #BonsaiClientMin
    def __init__(self, bonsai_server):
        self.bonsai_server = bonsai_server

        self.register()

    def register(self):
        # TODO, register with Bonsai Server
        pass

    def run(self, data):
        try:
            logger.info("Recieved Data")

            metrics = bonsai_pb2.MetricsRequest(id=data["id"] + data["jobname"], 
                                        job=data["jobname"], 
                                        host=data["hostname"], 
                                        metrics=json.dumps(data["metrics"]).encode('utf-8'),
                                        labels=data["labels"]
                                        )

            start_channel = time.time()
            with grpc.insecure_channel(self.bonsai_server) as channel:
                stub = bonsai_pb2_grpc.ServerStub(channel)
                response = stub.PushMetrics(metrics)
            end_channel = time.time()

            logger.info("[TIME] Transfer: %fs" % (end_channel - start_channel))
            logger.info("Recv: %d" % response.code)
        except Exception as e:
            print(e)

    
    
