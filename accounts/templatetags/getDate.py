from django.template import Library
from dateutil import parser

register = Library()

@register.filter(expects_localtime=True)
def getDate(data):
    return(parser.parse(data))