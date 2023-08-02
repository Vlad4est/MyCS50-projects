import requests

from flask import render_template
import hashlib

def apology(message, code=400):

    def escape(s):

        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def get_hashed_password(password):
    hashed_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    return hashed_password

def request_data(first5):
    url = "https://api.pwnedpasswords.com/range/" + first5
    res = requests.get(url)
    return res

def get_leaks_count(res, remaning):
    status_code = res.status_code
    if status_code != 200:
        return -1, res.status_code
    res = (i.split(":") for i in res.text.splitlines())
    for hash, count in res:
        if hash == remaning:
            return count, status_code
    return 0, status_code

def api_check(password):
    hashed_password = get_hashed_password(password)
    first5 , remaning = hashed_password[:5], hashed_password[5:]
    res = request_data(first5)
    return get_leaks_count(res, remaning)