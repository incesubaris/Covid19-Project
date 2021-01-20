from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    current_app,
)

# from flask_mysqldb import MySQL
# import MySQLdb.cursors
# import re
import psycopg2

# import re
import random

dsn = "postgres://cmwnxxaaygjldp:31b8a72313d52d8366f032b9ad669f7e91cef2aa3290866caf09345f84c562f1@ec2-52-2-6-71.compute-1.amazonaws.com:5432/d37b6b1t8t884a"
conn = psycopg2.connect(dsn)
cursor = conn.cursor()


def index():
    cursor.execute("SELECT COUNT(*) FROM patient;")
    a = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM test;")
    b = cursor.fetchone()
    cursor.execute("SELECT COUNT(*) FROM hospital;")
    c = cursor.fetchone()
    cursor.execute("SELECT SUM(capacity) FROM hospital;")
    d = cursor.fetchone()
    return render_template("index.html", a=a, b=b, c=c, d=d)


def login():
    # mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "TCKN" in request.form
        and "password" in request.form
    ):
        TCKN = request.form["TCKN"]
        password = request.form["password"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM patient WHERE tckn = '{0}' AND password = '{1}';".format(
                TCKN, password
            )
        )
        account = cursor.fetchone()
        if account:
            session["loggedin"] = True
            session["tckn"] = account[0]
            session["name"] = account[1]
            session["surname"] = account[2]
            session["age"] = account[3]
            session["gender"] = account[4]
            session["phone"] = account[5]
            session["adress"] = account[6]
            msg = "Logged in successfully !"
            return redirect(url_for("profile"))
            # return redirect(url_for('profil'),id=account[0])
        else:
            msg = "Incorrect username / password !"
    return render_template("login.html", msg=msg)


def logout():
    session["loggedin"] = False
    return redirect(url_for("index"))


def register():
    # mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "TCKN" in request.form
        and "name" in request.form
        and "surname" in request.form
        and "age" in request.form
        and "gender" in request.form
        and "phone" in request.form
        and "adress" in request.form
        and "password" in request.form
    ):
        TCKN = request.form["TCKN"]
        name = request.form["name"]
        surname = request.form["surname"]
        age = request.form["age"]
        gender = request.form["gender"]
        phone = request.form["phone"]
        adress = request.form["adress"]
        password = request.form["password"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM patient WHERE tckn = '{0}';".format(TCKN))
        account = cursor.fetchone()
        if account:
            msg = "TCKN already exists !"
        # elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        # msg = "Invalid email address !"
        # elif not re.match(r"[A-Za-z0-9]+", username):
        # msg = "Username must contain only characters and numbers !"
        elif (
            not TCKN or not name or not surname or not age or not gender or not password
        ):
            msg = "Please fill out the form !"
        else:
            cursor.execute(
                "INSERT INTO patient (TCKN ,name, surname, age, gender, phone, adress, password) VALUES ('{0}', '{1}', '{2}', {3},'{4}','{5}','{6}','{7}');".format(
                    TCKN, name, surname, age, gender, phone, adress, password
                )
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully registered !"
    elif request.method == "POST":
        msg = "Please fill out the form !"
    return render_template("register.html", msg=msg)


def profile():
    cursor.execute("SELECT * FROM patient WHERE tckn = '{0}';".format(session["tckn"]))
    patient = cursor.fetchone()
    if patient:
        return render_template("profile.html", patient=patient)
    else:
        return render_template("index.html")


def test():
    cursor.execute("SELECT * FROM hospital ORDER BY id ASC;")
    hastaneler = cursor.fetchall()
    if (
        request.method == "POST"
        and "hospital" in request.form
        and "date" in request.form
    ):
        TCKN = session["tckn"]
        hospital = request.form["hospital"]
        test_date = request.form["date"]
        r = random.randint(0, 9)
        if r < 3:  # Positive rate %30
            result = "p"
        else:
            result = "n"

        cursor.execute(
            "INSERT INTO test(patient, hospital, test_date, result) VALUES ('{0}', {1}, '{2}', '{3}');".format(
                TCKN, hospital, test_date, result
            )
        )

        # mysql.connection.commit()
        conn.commit()
        # cursor.close()
    return render_template("test.html", hastaneler=hastaneler)


def testsonuc():
    cursor.execute(
        "SELECT id, hospital, test_date, result FROM test WHERE patient = '{0}';".format(
            session["tckn"]
        )
    )
    info = cursor.fetchall()
    return render_template("testsonuc.html", info=info)


def update():
    ##mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "password" in request.form
        and "newpassword" in request.form
    ):
        password = request.form["password"]
        newpassword = request.form["newpassword"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            "SELECT * FROM patient WHERE tckn = '{0}' AND password = '{1}';".format(
                session["tckn"], password
            )
        )
        account = cursor.fetchone()
        if account:
            cursor.execute(
                "UPDATE patient SET password = '{0}' WHERE tckn = '{1}';".format(
                    newpassword, session["tckn"]
                )
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully changed password!"

        else:
            msg = "şifre hatalı"
    return render_template("update.html", msg=msg)


def delete():
    # mysql = current_app.config["mysql"]
    msg = ""
    if request.method == "POST" and "password" in request.form:
        password = request.form["password"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor) # şifre kontorlü
        cursor.execute(
            "SELECT * FROM patient WHERE tckn = '{0}' AND password = '{1}';".format(
                session["tckn"], password
            )
        )
        account = cursor.fetchone()
        if account:
            cursor.execute(
                "DELETE FROM test WHERE patient = '{0}';".format(session["tckn"])
            )
            cursor.execute(
                "DELETE FROM patient WHERE tckn = '{0}';".format(session["tckn"])
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully deleted !"
            logout()
        else:
            msg = "Şifrenizi giriniz"
    return render_template("delete.html", msg=msg)


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


def hastane():
    return render_template("hastane.html")


def hastaneekle():
    if (
        request.method == "POST"
        and "name" in request.form
        and "paramedic_count" in request.form
        and "capacity" in request.form
    ):
        name = request.form["name"]
        paramedic_count = request.form["paramedic_count"]
        capacity = request.form["capacity"]
        cursor.execute(
            "INSERT INTO hospital(name, paramedic_count, capacity) VALUES ('{0}', {1}, '{2}');".format(
                name, paramedic_count, capacity
            )
        )
        # mysql.connection.commit()
        conn.commit()

    return render_template("hastaneekle.html")


def hastanegoruntule():
    cursor.execute("SELECT * FROM hospital ORDER BY id ASC;")
    info = cursor.fetchall()
    return render_template("hastanegoruntuleme.html", info=info)
    ##mysql = current_app.config["mysql"]
    ##cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    ##query = "SELECT * FROM accounts;"
    ##cursor.execute(query)
    ##info = cursor.fetchall()
    ##return render_template("read.html", info=info)


def hastaneguncelleme():
    ##mysql = current_app.config["mysql"]
    msg = ""
    if (
        request.method == "POST"
        and "id" in request.form
        and "newcapacity" in request.form
    ):
        id = request.form["id"]
        newcapacity = request.form["newcapacity"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM hospital WHERE id = '{0}';".format(id))
        hospital = cursor.fetchone()
        if hospital:
            cursor.execute(
                "UPDATE hospital SET capacity = '{0}' WHERE id = {1};".format(
                    newcapacity, id
                )
            )
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully changed capacity!"

        else:
            msg = "hastane id yok"
    return render_template("hastaneguncelleme.html", msg=msg)


def hastanesilme():
    # mysql = current_app.config["mysql"]
    ##mysql = current_app.config["mysql"]
    msg = ""
    if request.method == "POST" and "id" in request.form:
        id = request.form["id"]
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM hospital WHERE id = '{0}';".format(id))
        hospital = cursor.fetchone()
        if hospital:
            cursor.execute("DELETE FROM test WHERE hospital = '{0}';".format(id))

            cursor.execute("DELETE FROM hospital WHERE id = '{0}';".format(id))
            conn.commit()
            # mysql.connection.commit()
            msg = "You have successfully deleted !"
        else:
            msg = "böyle hastane bulunamadı"
    return render_template("hastanesilme.html", msg=msg)


def admin():
    cursor.execute("SELECT * FROM patient;")
    patient = cursor.fetchall()
    cursor.execute("SELECT * FROM test;")
    test = cursor.fetchall()
    cursor.execute("SELECT * FROM hospital;")
    hospital = cursor.fetchall()
    return render_template("admin.html", patient=patient, test=test, hospital=hospital)
