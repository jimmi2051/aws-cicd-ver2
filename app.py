"""Main application file"""
from flask import Flask, Response
app = Flask(__name__)


@app.route("/")
def home():
    return Response("{'home':'this is api home'}", status=201, mimetype='application/json')


@app.route("/healthCheck")
def healthCheck():
    return Response("{'description':'the service is ok'}", status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
