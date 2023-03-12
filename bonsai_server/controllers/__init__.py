import os

from controllers.BonsaiLogger import *
from controllers.RethinkServer import RethinkServer
from controllers.RethinkServerConnection import RethinkServerConnection

from controllers.RethinkServerConnection import create_table, create_database

# create logger
logger = create_logger('bonsai')

# set rethinkdb connection location based on deployment env
if('IN_DOCKER_CONTAINER' in os.environ):
  dockerCheck = os.environ['IN_DOCKER_CONTAINER']
  if(os.environ['IN_DOCKER_CONTAINER']):
    rethink_server = "rethink"
else:
  rethink_server = "localhost"

rethink_database = "bonsai"
rethink_port = 28015

# create rethink server
rethink = RethinkServer(rethink_server=rethink_server, rethink_database=rethink_database, rethink_port=rethink_port)

# create default database
create_database(rethink_database, rethink)

# create default tables
create_table('metrics', rethink_database, rethink)
create_table('hosts', rethink_database, rethink)
create_table('dashboards', rethink_database, rethink)