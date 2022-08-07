import socket
import sched
import time
from datetime import datetime
import requests

import psutil

class BonsaiClient:
    def __init__(self, bonsai_server, jobname="demo", hostname=None, rate=5, exporters=[]):
        if(hostname == None):
            hostname = socket.gethostname()

        self.bonsai_server = bonsai_server
        self.jobname = jobname
        self.hostname = hostname
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
            data = self.build_request()
            print(data)

            r = requests.post(self.bonsai_server, json=data)
            print("[*] request status -", r.status_code)
        except Exception as e:
            print(e)

        self.event_loop.enter(self.rate, 5, self.run)

    def build_request(self):
        data = {
            "id": self.hostname + self.jobname,
            "job": self.jobname,
            "host": self.hostname,
            "metrics": {}
        }

        for exporter in self.exporters:
            data["metrics"][exporter.name] = exporter.get_metrics()

        return data

    
    