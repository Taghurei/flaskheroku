#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
import unidecode

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
