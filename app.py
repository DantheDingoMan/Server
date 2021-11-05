#!/usr/bin/env python3
"""
jokes api

make sure to catch post as well

"""
import json
from flask import Flask, Response, request, abort
from flask_cors import CORS, cross_origin
import pyjokes


app = Flask(__name__)
CORS(app)

@app.route("/api/v1/jokes")
def get_jokes():
    language = request.args['language']
    category = request.args['category']

    jokes = pyjokes.get_joke(language, category)
    res = Response(json.dumps({"joke": jokes}))
    res.headers["Content-Type"] = "application/json"
    return res



@app.route("/api/v1/joke")
def get_joke():
    language = request.args['language']
    category = request.args['category']
    id = request.args['id']
    ids = int(id)


    if ids < len(pyjokes.get_jokes(language, category)):
        joke = pyjokes.get_jokes(language, category)

        finaljoke = joke[ids]
    else: 
        abort(404)

    res = Response(json.dumps({"joke": finaljoke}))
    res.headers["Content-Type"] = "application/json"
    return res


if __name__ == "__main__":
    app.run("0.0.0.0")


