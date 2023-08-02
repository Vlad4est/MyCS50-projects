from flask import Flask, flash, redirect, render_template, request, session


app = Flask(__name__)

items = [1 , 12 ,31, 99 ,153 , 103]
@app.route("/")
def index():
    return render_template("index.html")