from flask import Flask
from address import Address

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "ParoquiaGo - Service"

@app.route("/get-churches")
def get_churches():
    address = Address()
    return address.get_data()