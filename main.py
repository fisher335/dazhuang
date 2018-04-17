#!/usr/bin/env python
# coding:utf-8
from bottle import Bottle, request, static_file
import os

app = Bottle()

abs_path = os.path.abspath('./static')
from router import *


# static_root = 'C:\mini\static'
@app.route('/static/<filename:path>')
def static_files(filename):
    return static_file(filename=filename, root=abs_path)


@app.route('/favicon.ico/')
def static_files_icon():
    return static_file(filename='favicon.ico', root=abs_path)


@app.route('/download/<img>')
def static_files_icon(img):
    return static_file(filename=img, root=os.path.join(abs_path, 'qrcode'), download=True)


if __name__ == '__main__':
    app.run(port=8080, debug=True, reloader=True, server="gevent")
