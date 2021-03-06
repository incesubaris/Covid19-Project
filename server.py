from flask import Flask, render_template, flash, redirect, url_for, request, session

# from flask_mysqldb import MySQL
# import psycopg2

from functools import wraps

# from passlib.hash import pbkdf2_sha256 as hasher
import psycopg2
import os
import views


dsn = "postgres://cmwnxxaaygjldp:31b8a72313d52d8366f032b9ad669f7e91cef2aa3290866caf09345f84c562f1@ec2-52-2-6-71.compute-1.amazonaws.com:5432/d37b6b1t8t884a"
con = psycopg2.connect(dsn)
cur = con.cursor()

app = Flask(__name__)


app.secret_key = "your secret key"

##app.config["MYSQL_HOST"] = "localhost"
##app.config["MYSQL_USER"] = "root"
##app.config["MYSQL_PASSWORD"] = "admin"
##app.config["MYSQL_DB"] = "deneme"
##app.config["MYSQL_CURSORCLASS"] = "DictCursor"

##mysql = MySQL(app)

##app.config["app"] = app
##app.config["mysql"] = mysql

app.add_url_rule("/", view_func=views.index, methods=["GET", "POST"])
app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=views.logout)
app.add_url_rule("/register", view_func=views.register, methods=["GET", "POST"])
app.add_url_rule("/profile", view_func=views.profile, methods=["GET", "POST"])
app.add_url_rule("/update", view_func=views.update, methods=["GET", "POST"])
app.add_url_rule("/delete", view_func=views.delete, methods=["GET", "POST"])
app.add_url_rule("/test", view_func=views.test, methods=["GET", "POST"])
app.add_url_rule("/testsonuc", view_func=views.testsonuc, methods=["GET", "POST"])
app.add_url_rule("/hastane", view_func=views.hastane, methods=["GET", "POST"])
app.add_url_rule("/hastaneekle", view_func=views.hastaneekle, methods=["GET", "POST"])
app.add_url_rule(
    "/hastanegoruntule", view_func=views.hastanegoruntule, methods=["GET", "POST"]
)
app.add_url_rule(
    "/hastaneguncelleme", view_func=views.hastaneguncelleme, methods=["GET", "POST"]
)
app.add_url_rule("/hastanesilme", view_func=views.hastanesilme, methods=["GET", "POST"])
##app.add_url_rule("/<int:id>", view_func=views.profile, methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)