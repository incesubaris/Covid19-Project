from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    current_app,
)
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import psycopg2

conn = psycopg2.connect("dbname=deneme user=postgres host=localhost password=admin")
cursor = conn.cursor()


def read():
    cursor.execute("SELECT * FROM accounts ORDER BY id ASC;")
    info = cursor.fetchall()
    return render_template("read.html", info=info)
    ##mysql = current_app.config["mysql"]
    ##cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    ##query = "SELECT * FROM accounts;"
    ##cursor.execute(query)
    ##info = cursor.fetchall()
    ##return render_template("read.html", info=info)


def index():
    return render_template("index.html")


def update():
    ##mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        newpassword = request.form["password"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM accounts WHERE username = '{0}';".format(username)
        )
        account = cursor.fetchone()
        if account:
            cursor.execute(
                "UPDATE accounts SET password = '{0}' WHERE username = '{1}';".format(
                    newpassword, username
                )
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully changed !"
        else:
            msg = "HESAP YOK LAN"
    return render_template("update.html", msg=msg)


def delete():
    # mysql = current_app.config["mysql"]
    msg = ""
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM accounts WHERE username = '{0}';".format(username)
        )
        account = cursor.fetchone()
        if account:
            cursor.execute(
                "DELETE FROM accounts WHERE username = '{0}';".format(username)
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully deleted !"
        else:
            msg = "HESAP YOK LAN"
    return render_template("delete.html", msg=msg)


def login():
    # mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM accounts WHERE username = '{0}' AND password = '{1}';".format(
                username, password
            )
        )
        account = cursor.fetchone()
        if account:
            session["loggedin"] = True
            session["id"] = account[1]
            session["username"] = account[2]
            msg = "Logged in successfully !"
            return render_template("index.html", msg=msg)
        else:
            msg = "Incorrect username / password !"
    return render_template("login.html", msg=msg)


def logout():
    session.pop("loggedin", None)
    session.pop("id", None)
    session.pop("username", None)
    return redirect(url_for("login"))


def register():
    # mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "email" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        # cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM accounts WHERE username = '{0}';".format(username)
        )
        account = cursor.fetchone()
        if account:
            msg = "Account already exists !"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            msg = "Invalid email address !"
        elif not re.match(r"[A-Za-z0-9]+", username):
            msg = "Username must contain only characters and numbers !"
        elif not username or not password or not email:
            msg = "Please fill out the form !"
        else:
            cursor.execute(
                "INSERT INTO accounts (username ,password, email) VALUES ('{0}', '{1}', '{2}');".format(
                    username, password, email
                )
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully registered !"
    elif request.method == "POST":
        msg = "Please fill out the form !"
    return render_template("register.html", msg=msg)
