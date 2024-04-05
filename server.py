
from flask import Flask, render_template
import sys

from DatabaseManager import *

app = Flask(__name__)
dbman = DatabaseManager("./volumes/ots.db")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/client/<clientID>")
def clientInfoPage(clientID):
    client = dbman.getClient(clientID)[0]
    return render_template("client.html", client=client)

app.run(host="0.0.0.0", port=8080)
