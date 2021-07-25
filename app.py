from flask import Flask,json
import logging
from datetime import datetime




app = Flask(__name__)

def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

@app.route('/status')
def healthcheck():
    status_response = {"result":"OK - healthy"}

    response = app.response_class(
        response=json.dumps(status_response),
        status=200,
        mimetype="application/json"
    )

    app.logger.info("\t[%s] /Status \tStatus request successful.",get_current_time())
    return response

@app.route('/metrics')
def metrics():
    data = {"userCount":200,"userAccountActive":23}
    response=  app.response_class(
        response=json.dumps({"status":"success","code":0,"data":data}),
        status=200,
        mimetype="application/json"
    )

    app.logger.info("\t[%s] /Metric \tMetric request successful.",get_current_time())
    return response

@app.route("/")
def hello():

    app.logger.info("\t[%s] / \t/ Index request successful.",get_current_time())
    return "Hello Flask!"

if __name__ == "__main__":
    logging.basicConfig(filename="app.log",level=logging.DEBUG)
    app.run(host='0.0.0.0')
