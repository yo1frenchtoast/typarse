#!/usr/bin/env python3
import json
from flask import Flask 

data = {}

input_file = "concerts_rennes"
with open(input_file+".json") as jsonfile:
    data = json.load(jsonfile)

app = Flask(__name__)

@app.route('/')
def get():
    return data

if __name__ == '__main__':
    app.run()