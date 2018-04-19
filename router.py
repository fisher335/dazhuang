# -*- coding: utf-8 -*-
# @Date    : '2018/4/16 0016'
# @Author  : Terry feng  (fengshaomin@qq.com)
from main import app
from bottle import request, template, redirect
import qrcode
import os, time
from random import randint


@app.route("/test/")
def test():
    print("7777")
    return "hello test"


@app.route("/file/")
def test():
    return template("file")


@app.get('/list/')
def upload():
    return template('list', session=request.headers)


@app.get('/wiki/')
def upload():
    redirect("https://github.com/fisher335/wiki/issues")
    return None


@app.route('/')
@app.route('/index/')
@app.route('/qrcode/', method=['GET'])
def index():
    return template("index")


@app.post('/qrcode/')
@app.route('/qrcode/<img>', method=['GET', 'POST'])
def qrcodelike(img=None):
    if img == "":
        template("index")
    url = request.forms.url
    print(url.encode("utf-8"))
    # img_name = url.replace("/", "")
    # img_name = img_name.replace(":", "")
    img_name = randint(1, 1000000)
    imge = qrcode.make(url)
    imge.save(os.path.join("static/qrcode", str(img_name) + ".png"))
    return template('qrcode', img=img_name)
