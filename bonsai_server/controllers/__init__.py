import os

from controllers.BonsaiLogger import *
from controllers.RethinkServer import RethinkServer
from controllers.RethinkServerConnection import RethinkServerConnection

from controllers.RethinkServerConnection import create_table, create_database

# logger
logger = create_logger('bonsai')

if('IN_DOCKER_CONTAINER' in os.environ):
  dockerCheck = os.environ['IN_DOCKER_CONTAINER']
  if(os.environ['IN_DOCKER_CONTAINER']):
    rethink_server = "rethink"
else:
  rethink_server = "localhost"

rethink_database = "bonsai"
rethink_port = 28015

rethink = RethinkServer(rethink_server=rethink_server, rethink_database=rethink_database, rethink_port=rethink_port)

create_database(rethink_database, rethink)

create_table('metrics', rethink_database, rethink)
create_table('hosts', rethink_database, rethink)
create_table('dashboards', rethink_database, rethink)