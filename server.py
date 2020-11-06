from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def homepage():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=day_name)


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
