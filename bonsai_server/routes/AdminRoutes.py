from flask_restful import Resource, Api

from controllers import RethinkServerConnection, rethink

class AdminPurge(Resource):
    def get(self):
        print(rethink)
        with RethinkServerConnection(rethink) as conn:
            rethink.r.table("metrics").delete().run(conn)

        return {"status": 200}