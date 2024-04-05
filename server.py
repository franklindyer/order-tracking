
from flask import Flask, render_template
import sys

from DatabaseManager import *
from formatting import formatters

app = Flask(__name__)
dbman = DatabaseManager("./volumes/ots.db")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/client/<clientID>")
def clientInfoPage(clientID):
    client = dbman.getClient(int(clientID))
    return render_template("client.html", client=client, **formatters)

@app.route("/product/<productID>")
def productInfoPage(productID):
    product = dbman.getProduct(int(productID))
    return render_template("product.html", product=product, **formatters)

@app.route("/order/<orderID>")
def orderInfoPage(orderID):
    order = dbman.getOrder(int(orderID))
    return render_template("order.html", order=order, **formatters)

@app.route("/orders")
def orderSearchPage():
    orders = dbman.getOrders()
    return render_template("orders.html", orders=orders, **formatters)

app.run(host="0.0.0.0", port=8080)
