from flask import Flask
from api.address import Address
from api.news import News

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "ParoquiaGo - Service"

@app.route("/get-churches")
def get_churches():
    address = Address()
    return address.get_data()

@app.route("/get-news")
def get_news():
    news = News()
    return news.get_news()