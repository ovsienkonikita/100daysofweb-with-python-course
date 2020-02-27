from time import time

from flask import render_template

from . import app

visits_num = 0


@app.route("/")
def index():
    global visits_num
    visits_num += 1
    return render_template("index.html", unix_time=time())


@app.route("/visits")
def visits():
    global visits_num
    return render_template("visits.html", visits_number=visits_num)


@app.route("/corona")
def corona():
    pass
