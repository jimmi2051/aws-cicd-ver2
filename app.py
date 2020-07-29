"""Main application file"""
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return {
        "home": "Home is ok."
    }


@app.route("/healthCheck")
def healthCheck():
    return {
        "description": "service is ok."
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
