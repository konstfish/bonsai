import logging

from datetime import datetime

from flask import request
from flask_restful import Resource, Api, reqparse

from controllers import RethinkServerConnection, rethink

logger = logging.getLogger('bonsai')

class MetricsPush(Resource):
    def post(self):
        rjson = request.get_json()
        rjson["date"] = str(datetime.now())

        with RethinkServerConnection(rethink_server=rethink) as conn:
            out = rethink.r.table("metrics").insert(rjson, conflict="update").run(conn)
            logger.debug(out)

        return {"status": "200"}