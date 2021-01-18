from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import views

app = Flask(__name__)


app.secret_key = "your secret key"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "deneme"
##app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

app.config["app"] = app
app.config["mysql"] = mysql

app.add_url_rule("/", view_func=views.index, methods=["GET", "POST"])
app.add_url_rule("/read", view_func=views.read, methods=["GET", "POST"])
app.add_url_rule("/update", view_func=views.update, methods=["GET", "POST"])
app.add_url_rule("/delete", view_func=views.delete, methods=["GET", "POST"])
app.add_url_rule("/logout", view_func=views.logout)
app.add_url_rule("/login", view_func=views.login, methods=["GET", "POST"])
app.add_url_rule("/register", view_func=views.register, methods=["GET", "POST"])


if __name__ == "__main__":
    app.run()