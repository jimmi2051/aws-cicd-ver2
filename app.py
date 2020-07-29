"""Main application file"""
from flask import Flask
app = Flask(__name__)


@app.route('/<random_string>')
def returnBackwardsString(random_string):
    """Reverse and return the provided URI"""
    return "".join(reversed(random_string))


@app.route("/")
def home():
    return {
        "description": "service is ok."
    }


@app.route("/healthCheck")
def healthCheck():
    return {
        "description": "service is ok."
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
