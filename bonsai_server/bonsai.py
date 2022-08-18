import logging

from flask import Flask, request
from flask_restful import Resource, Api

import controllers
import routes

logger = logging.getLogger('bonsai')

# mdbc = pymongo.MongoClient('mongodb://database:27017/')
# r.db("test").table_create("authors").run())

app = Flask(__name__)
api = Api(app)

# metric routes
api.add_resource(routes.MetricsPush, '/push')

api.add_resource(routes.MetricAmount, '/metric/amount')

# admin routes
api.add_resource(routes.AdminPurge, '/admin/purge')

if __name__ == '__main__':
  port = 4000
  logger.info("🌳 Started Bonsai on :" + str(port))
  app.run(host="0.0.0.0", port=port)

if __name__ == 'bonsai':
  port = 4000
  logger.info("🌳 Started Bonsai on :" + str(port))
