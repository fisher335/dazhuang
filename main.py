#!/usr/bin/env python
# coding:utf-8
from bottle import Bottle, request, static_file, template, redirect, HTTPResponse
import os, time

app = Bottle()
from router import *

abs_path = os.path.abspath('./static')


# static_root = 'C:\mini\static'
@app.route('/static/<filename:path>')
def static_files(filename):
    return static_file(filename=filename, root=abs_path)


@app.route('/favicon.ico/')
def static_files_icon():
    return static_file(filename='favicon.ico', root=abs_path)


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000, debug=True, reloader=True)
    app.run(port=8080, debug=True, reloader=True, server="gevent")
