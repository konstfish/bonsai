from flask import Flask
from flask import request

from rethinkdb import RethinkDB
r = RethinkDB()

# mdbc = pymongo.MongoClient('mongodb://database:27017/')

conn = r.connect( "localhost", 28015, db="bonsai")
#r.db("test").table_create("authors").run()

try:
  r.db_create('bonsai').run(conn)
except:
  pass

try:
  r.db('bonsai').table_create('metrics').run(conn)
except:
  pass

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/push", methods=["POST"])
def push():
    rjson = request.get_json()

    #test = r.table('metrics').filter({"host": rjson["host"], "job": rjson["job"]}).run(conn)

    print(r.table('metrics').insert(rjson, conflict="update").run(conn))

    #r.table("metrics").filter({"job": rjson[job], "host": rjson[host]}).update(rjson).run()

    print(request)

    return "<p>Hello, World!</p>"

app.run(host="0.0.0.0", port=4000)