import socket
import sched
import time
from datetime import datetime
import requests

import psutil

class BonsaiClient:
    def __init__(self, bonsai_server, jobname="demo", hostname=None, rate=5):
        if(hostname == None):
            hostname = socket.gethostname()

        self.bonsai_server = bonsai_server
        self.jobname = jobname
        self.hostname = hostname
        self.rate = rate # [s]

        # loop
        self.event_loop = sched.scheduler(time.time, time.sleep)
        self.run()
        self.event_loop.run()

    def run(self):
        try:
            r = requests.post(self.bonsai_server, json={
                "id": self.hostname + self.jobname,
                "job": self.jobname,
                "host": self.hostname,
                "values": {
                    "value": str(datetime.now()),
                    "cpu": psutil.cpu_percent(),
                    "mem": psutil.virtual_memory().percent
                },
            })
            print("[*] request status -", r.status_code)
        except Exception as e:
            print(e)

        self.event_loop.enter(self.rate, 5, self.run)

    
    