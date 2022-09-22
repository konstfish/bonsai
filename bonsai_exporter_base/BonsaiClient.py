import socket
import sched
import time
from datetime import datetime

import psutil

import proto
import json
import grpc
import bonsai_pb2
import bonsai_pb2_grpc

class BonsaiClient:
    def __init__(self, bonsai_server, jobname="demo", hostname=None, rate=5, exporters=[]):
        if(hostname == None):
            hostname = socket.gethostname()

        self.bonsai_server = bonsai_server
        self.jobname = jobname
        self.hostname = hostname
        self.labels = {'type': 'test'}
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
            with grpc.insecure_channel(self.bonsai_server) as channel:
                stub = bonsai_pb2_grpc.ServerStub(channel)
                metrics = self.build_request()
                response = stub.PushMetrics(metrics)
                
            print("Recv: ", response.code)
        except Exception as e:
            print(e)

        self.event_loop.enter(self.rate, 5, self.run)

    def build_request(self):
        data = {}
        for exporter in self.exporters:
            data[exporter.name] = exporter.get_metrics()

        metric_req = bonsai_pb2.MetricsRequest(id=self.hostname + self.jobname, 
                                        job=self.jobname, 
                                        host=self.hostname, 
                                        metrics=json.dumps(data).encode('utf-8'),
                                        labels=self.labels
                                        )

        return metric_req

    
    