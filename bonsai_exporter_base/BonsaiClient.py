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

import time
from datetime import datetime

import psutil

import proto
import json
import grpc
import bonsai_pb2
import bonsai_pb2_grpc

class BonsaiClient:
    def __init__(self, bonsai_server, jobname="demo", hostname=None, rate=5, labels=[], exporters=[]):
        if(hostname == None):
            hostname = socket.gethostname()

        self.bonsai_server = bonsai_server
        self.jobname = jobname
        self.hostname = hostname
        self.labels = labels
        self.rate = rate # [s]

        self.exporters = exporters

        self.register()

        # loop
        self.event_loop = sched.scheduler(time.time, time.sleep)
        self.run()
        self.event_loop.run()

    def register(self):
        # TODO, register with Bonsai Server
        pass

    def run(self):
        try:
            start_metrics = time.time()
            metrics = self.build_request()
            end_metrics = time.time()

            logger.info("[TIME] Scraping: %fs" % (end_metrics - start_metrics))

            start_channel = time.time()
            with grpc.insecure_channel(self.bonsai_server) as channel:
                stub = bonsai_pb2_grpc.ServerStub(channel)
                response = stub.PushMetrics(metrics)
            end_channel = time.time()

            logger.info("[TIME] Transfer: %fs" % (end_channel - start_channel))
            logger.info("Recv: %d" % response.code)
        except Exception as e:
            print(e)

        self.event_loop.enter(self.rate, 1, self.run)

    def build_request(self):
        data = {}
        for exporter in self.exporters:
            data[exporter.name] = exporter.get_metrics()

        #for label in self.labels:
        #    metric_labels = bonsai_pb2.MetricLabels()
        #    metric_labels.label.extend(self.labels[label])
        
        """
        print(
            {"id": self.hostname + self.jobname, 
             "job": self.jobname,
             "host": self.hostname,
             "metrics": data,
             "labels": self.labels
            }
        )
        """

        #print(json.dumps(data).encode('utf-8'))
        metric_req = bonsai_pb2.MetricsRequest(id=self.hostname + self.jobname, 
                                        job=self.jobname, 
                                        host=self.hostname, 
                                        metrics=json.dumps(data).encode('utf-8'),
                                        labels=self.labels
                                        )

        return metric_req

    
    
