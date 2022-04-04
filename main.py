
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome</h1>"

@app.route("/contact")
def ContactUs():
    return render_template("Admin.html")

@app.route("/Search")
def Search():
    return render_template("Search.html")

@app.route("/Delete")
def Delete():
    return render_template("Delete.html")

if __name__ == "__main__":
    app.run()