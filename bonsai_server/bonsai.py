import logging

from datetime import datetime

from flask import Flask
from flask import request

from rethinkdb import RethinkDB
r = RethinkDB()

logger = logging.getLogger('bonsai_logger')
logger.setLevel(logging.DEBUG)

default_handler = logging.StreamHandler()
default_handler.setFormatter(
    logging.Formatter("[%(asctime)s]   [%(process)d] [%(levelname)s] [%(module)s] %(message)s")
)
logger.addHandler(default_handler)

#rethink_server = "rethink"
rethink_server = "10.0.1.108"
rethink_port = 28015
rethink_database = "bonsai"

# mdbc = pymongo.MongoClient('mongodb://database:27017/')
#r.db("test").table_create("authors").run())

class RethinkServerConnection():
  def __init__(self):
    self.conn = 0
      
  def __enter__(self):
    self.conn = r.connect( rethink_server, rethink_port, db=rethink_database)
    return self.conn
  
  def __exit__(self, *args, **kwargs):
    self.conn.close()

with RethinkServerConnection() as conn:
  if(rethink_database not in r.db_list().run(conn)):
    logger.info('Creating DB: ' + rethink_database)
    r.db_create(rethink_database).run(conn)
  else:
    logger.info('DB ' + rethink_database + ' already exists, skipping')

  if('metrics' not in r.db(rethink_database).table_list().run(conn)):
    logger.info('Creating Table: ' + rethink_database)
    r.db(rethink_database).table_create('metrics').run(conn)
  else:
    logger.info('Table ' + 'metrics' + ' already exists, skipping')

app = Flask(__name__)

@app.route("/")
def hello_world():
  logging.info('this is an INFO message')
  app.logger.warning('this is a WARNING message')
  return "<p>Hello, World!</p>"
  

@app.route("/push", methods=["POST"])
def push():
  rjson = request.get_json()
  rjson["date"] = str(datetime.now())

  #test = r.table('metrics').filter({"host": rjson["host"], "job": rjson["job"]}).run(conn)

  with RethinkServerConnection() as conn:
    print(r.table("metrics").insert(rjson, conflict="update").run(conn))

  #r.table("metrics").filter({"job": rjson[job], "host": rjson[host]}).update(rjson).run()

  print(request)

  return {"status": "200"}

@app.route("/api/admin/purge")
def admin_purge():
  with RethinkServerConnection() as conn:
    r.table("metrics").delete().run(conn)
  
  return {"status": "200"}

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=4000)