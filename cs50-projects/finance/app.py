import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, type_of_transaction

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    stocks = db.execute("SELECT symbol, company_name, shares FROM user_stocks WHERE user_id=?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
    cash = float(cash[0]["cash"])
    return render_template("index.html", stocks=stocks, lookup=lookup, cash=cash, usd=usd)





@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("Value not a number")

        if symbol == "":
            return apology("Missing symbol")
        if int(shares) < 1:
            return apology("Too few shares")
        

        quote = lookup(symbol)

        if quote is None:
            return apology("The symbol dosen't exist")

        check = db.execute("SELECT symbol, shares FROM user_stocks WHERE user_id=?", session["user_id"])
        user_balance = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
        user_balance = user_balance[0]["cash"]
        user_balance -= int(shares) * float(quote["price"])
        if user_balance < 0:
            return apology("You don't have enought money!")

        for stock in check:
            if quote["symbol"] == stock["symbol"]:
                shares += int(stock["shares"])
                db.execute("UPDATE user_stocks SET shares=? WHERE user_id=? AND symbol=?;", shares, session["user_id"], quote["symbol"])
                db.execute("UPDATE users SET cash=? WHERE id=?", user_balance, session["user_id"])
                db.execute("INSERT INTO user_transactions (user_id, symbol, shares, price, type) VALUES (?, ?, ?, ?, ?);", session["user_id"], quote["symbol"], shares, quote["price"], "buy")
                return redirect("/")

        db.execute("INSERT INTO user_stocks (user_id, symbol, company_name, shares) VALUES (?, ?, ?, ?);", session["user_id"], quote["symbol"], quote["name"], shares)
        db.execute("UPDATE users SET cash=? WHERE id=?", user_balance, session["user_id"])
        db.execute("INSERT INTO user_transactions (user_id, symbol, shares, price, type) VALUES (?, ?, ?, ?, ?);", session["user_id"], quote["symbol"], shares, quote["price"], "buy")
        return redirect("/")

    if request.method == "GET":
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    transactions = db.execute("SELECT symbol, shares, price, transacted, type FROM user_transactions WHERE user_id=?", session["user_id"])
    return render_template("history.html" , transactions=transactions, type_of_transaction=type_of_transaction, usd=usd)



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if symbol == "":
            return apology("Missing symbol")
        quote = lookup(symbol)
        if quote is None:
            return apology("The symbol dosen't exist")

        return render_template("quoted.html", name=quote["name"], price=usd(quote["price"]), symbol=quote["symbol"])

    if request.method == "GET":
        return render_template("quote.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")


        if username == "" or password == "" or confirmation =="":
            return(apology("Make sure you provide a username, password and password confirmation!"))

        if password != confirmation:
            return(apology("The passwords don't match"))


        check_username = db.execute("SELECT * FROM users WHERE username=?",username)
        if check_username != []:
            return(apology("The username is in use"))


        hashed_password = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username ,hashed_password)
        id = db.execute("SELECT id FROM users WHERE username=?", username)
        id = id[0]["id"]
        session["user_id"] = id
        return redirect("/")

    if request.method == "GET":
        return render_template("registration.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():

    if request.method == "POST":
            symbol = request.form.get("symbol")
            shares = request.form.get("shares")
            try:
                shares = int(shares)
            except ValueError:
                return apology("Enter a number")

            if shares < 1:
                return apology("Shares must be positive")

            user_shares = db.execute("SELECT shares FROM user_stocks WHERE symbol=? AND user_id=?", symbol, session["user_id"])
            if user_shares == []:
                return apology("You don't own shares at this company!")

            user_shares = user_shares[0]["shares"]
            if shares > user_shares:
                return apology("Too many shares")

            total_shares = user_shares - shares
            quote = lookup(symbol)
            price = float(quote["price"])
            user_balance = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
            user_balance = float(user_balance[0]["cash"]) + price * shares
            db.execute("UPDATE user_stocks SET shares=? WHERE symbol=?", total_shares, symbol)
            db.execute("UPDATE users SET cash=? WHERE id=?", user_balance, session["user_id"])
            db.execute("INSERT INTO user_transactions (user_id, symbol, shares, price, type) VALUES (?, ?, ?, ?, ?);", session["user_id"], symbol, shares, price, "sell")
            return redirect("/")

    if request.method == "GET":
        symbols = db.execute("SELECT symbol, shares FROM user_stocks WHERE user_id=?;", session["user_id"])
        return render_template("sell.html", symbols=symbols)
    return apology("TODO")


@app.route("/balance", methods=["GET", "POST"])
@login_required
def balance():
    balance = db.execute("SELECT cash FROM users WHERE id=?", session["user_id"])
    balance = float(balance[0]["cash"])
    if request.method == "POST":
        option = request.form.get("option")
        amount = float(request.form.get("amount"))
        if option == "Set":
            balance = amount
        if  option == "Deposit":
            balance += amount
        if option == "Withdrawl":
            balance -= amount
            if balance < 0:
                return apology("You don't have enough cash!")
        db.execute("UPDATE users SET cash=? WHERE id=?", balance, session["user_id"])
        return redirect("/balance")

    if request.method == "GET":
        return render_template("balance.html", balance=balance, usd=usd)