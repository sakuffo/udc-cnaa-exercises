from flask import Flask
from flask import json
import logging

app = Flask(__name__)
logging.basicConfig(filename="app.log", level=logging.INFO, format= '%(asctime)s, %(message)s')

@app.route("/")
def hello():
    app.logger.info("/ endpoint was reached")
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info("/status endpoint was reached")
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"data": {
            "User Count": "140", "UserCount Active": "23",
        }}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info("/metrics endpoint was reached")
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
