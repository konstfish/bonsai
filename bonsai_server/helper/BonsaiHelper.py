import logging

import sched

import time
from datetime import datetime

from controllers import RethinkServerConnection, rethink

logger = logging.getLogger('bonsai')

class BonsaiHelper:
    def __init__(self):
        logger.info("Init Bonsai Helper")

    def run(self):
        while True: 
            print("asdf")
            time.sleep(1)