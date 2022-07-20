import sched
import time
from datetime import datetime
import requests
import psutil

event_schedule = sched.scheduler(time.time, time.sleep)

def do_something():
    try:
        r = requests.post('http://server:4000/push', json={
        "id": "demolocalhost",
        "values": {
            "value": str(datetime.now()),
            "cpu": psutil.cpu_percent(),
            "mem": psutil.virtual_memory().percent
        },
        "job": "demo",
        "host": "localhost"
        })
        print("sent request")
    except:
        print("err")

    event_schedule.enter(1, 1, do_something)


do_something()

event_schedule.run()
