from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Abcd.1234'
app.config['MYSQL_DB'] = 'BLG317'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form

        tckn = int(details['TCKN'])
        ad = details['name']
        soyad = details['surname']
        yas = int(details['age'])
        cinsiyet = details['gender']
        telefon = int(details['phone'])
        adres = details['adress']
        hastalık = int(details['illness'])

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO patient(TCKN, name, surname, age, gender, phone, adress, illness)VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (tckn, ad, soyad, yas, cinsiyet, telefon, adres, hastalık))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
