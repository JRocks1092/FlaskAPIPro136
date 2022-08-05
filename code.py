from flask import Flask, jsonify, request
from flask_cors import CORS
from data import data


app = Flask(__name__)
CORS(app)


@app.route("/")
def root():
    return jsonify({"data": data, "message": "star data"})


@app.route("/star")
def planet():
    req = request.args.get("name")
    planetdata = []
    for i in data:
        if i.get("name") == req:
            planetdata.append(i)
    return jsonify({"data": planetdata, "message": "star data"})


if __name__ == "__main__":
    app.run()
