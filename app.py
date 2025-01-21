#!/usr/bin/env python3
from lib import typarse
from flask import Flask 
import json

app = Flask(__name__)

@app.route('/<ville>')
def get(ville):
    data = typarse.parse(ville)
    return data

if __name__ == '__main__':
    app.run()