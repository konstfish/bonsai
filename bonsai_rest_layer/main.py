from BonsaiClient import BonsaiClient
from flask import Flask, request

client = BonsaiClient("server:50051")

app = Flask(__name__)

@app.route("/pushMetrics", methods=["POST"])
def import_streak_csv():
    args = request.get_json()
    client.run(args)

    return {"status": 200}

app.run(host="0.0.0.0", port=4000)
