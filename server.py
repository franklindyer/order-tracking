
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
    client = dbman.getClient(clientID)
    return render_template("client.html", client=client)

@app.route("/product/<productID>")
def productInfoPage(productID):
    product = dbman.getProduct(productID)
    return render_template("product.html", product=product)

@app.route("/order/<orderID>")
def orderInfoPage(orderID):
    order = dbman.getOrder(orderID)
    return render_template("order.html", order=order)

app.run(host="0.0.0.0", port=8080)
