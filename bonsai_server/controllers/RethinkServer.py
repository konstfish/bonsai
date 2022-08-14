from rethinkdb import RethinkDB

class RethinkServer():
  def __init__(self, rethink_server="rethink", rethink_database="bonsai", rethink_port=28015):
    self.r = RethinkDB()

    self.rethink_server = rethink_server
    self.rethink_port = rethink_port
    self.rethink_database = rethink_database

