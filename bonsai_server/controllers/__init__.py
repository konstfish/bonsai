import os

from controllers.BonsaiLogger import *
from controllers.RethinkServer import RethinkServer
from controllers.RethinkServerConnection import RethinkServerConnection

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

with RethinkServerConnection(rethink) as conn:
  if(rethink_database not in rethink.r.db_list().run(conn)):
    logger.info('Creating DB: ' + rethink_database)
    rethink.r.db_create(rethink_database).run(conn)
  else:
    logger.info('DB ' + rethink_database + ' already exists, skipping')

  if('metrics' not in rethink.r.db(rethink_database).table_list().run(conn)):
    logger.info('Creating Table: ' + rethink_database)
    rethink.r.db(rethink_database).table_create('metrics').run(conn)
  else:
    logger.info('Table ' + 'metrics' + ' already exists, skipping')
