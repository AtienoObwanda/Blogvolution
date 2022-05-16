import urllib.request,json
from .models import Quote

# get randorm Quote
randormUrl = "http://quotes.stormconsultancy.co.uk/random.json"
def getRandorm():
    with urllib.request.urlopen(randormUrl) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)
        quote_object = None

        if quote_details_response:
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')
            quote_object = Quote(author, quote)
            return quote_object

# get popular quotes

popularUrl = "http://quotes.stormconsultancy.co.uk/popular.json"
def getPopular():
     with urllib.request.urlopen('popularUrl') as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)
        pquote_object = None

        if quote_details_response:
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')
            pquote_object = Quote(author, quote)
            return pquote_object
