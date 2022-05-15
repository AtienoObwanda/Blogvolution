from flask import requests
from .models import Quote

# get randorm Quote
randormUrl = "http://quotes.stormconsultancy.co.uk/random.json"
def getRandorm():
    response = requests.get(randormUrl).json()
    randomQuote = Quote(response.get("author"), response.get("quote"))
    return randomQuote

# get new quotes

popularUrl = "http://quotes.stormconsultancy.co.uk/popular.json"
def getPopular():
    response = requests.get(popularUrl).json()
    popularQuote = Quote(response.get("author"), response.get("quote"))
    return popularQuote