from rethinkdb import RethinkDB
from controllers.RethinkServer import RethinkServer

class RethinkServerConnection():
  def __init__(self, rethink_server: RethinkServer):
    self.rethink_server = rethink_server
    self.conn = 0
      
  def __enter__(self):
    self.conn = self.rethink_server.r.connect(  self.rethink_server.rethink_server, 
                                                self.rethink_server.rethink_port, 
                                                db=self.rethink_server.rethink_database)
    return self.conn
  
  def __exit__(self, *args, **kwargs):
    self.conn.close()


"""
from rethinkdb import RethinkDB

class RethinkServerConnection():
  def __init__(self, rethink_server="rethink", rethink_port=28015, rethink_database="bonsai"):
    self.conn = 0
    self.r = RethinkDB()

    self.rethink_server = rethink_server
    self.rethink_port = rethink_port
    self.rethink_database = rethink_database
      
  def __enter__(self):
    self.conn = self.r.connect( self.rethink_server, self.rethink_port, db=self.rethink_database)
    return self.conn
  
  def __exit__(self, *args, **kwargs):
    self.conn.close()
  
"""