from flask import Flask, render_template, request

from helpers import api_check, apology
from password_generator import generate_password



app = Flask(__name__)
app.debug = True


@app.route("/", methods =["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")

    if request.method == "POST":
        password = request.form.get("password")
        count, status_code = api_check(password)
        if status_code != 200:
            return apology(f"Problem with API", status_code)
        return render_template("result.html", count = count, password = password)


@app.route("/generator", methods = ["GET", "POST"])
def generator():
    if request.method == "GET":
        return render_template("generator.html")

    if request.method == "POST":
        min_lenght = int(request.form.get("passwordLenght"))
        if request.form.get("includeNumber") == "on":
            include_numbers = True
        else:
            include_numbers = False

        if request.form.get("includeSpecial") == "on":
            include_special = True
        else:
            include_special = False

        password = generate_password(min_lenght, include_numbers, include_special)
        return render_template("generator.html", password=password)
