from django.template import Library
import requests
from urllib.parse import unquote, quote
register = Library()

@register.filter(expects_localtime=True)
def getUrl(data):
    r = requests.get(unquote(data))
    print(r.url)
    return quote(r.url)