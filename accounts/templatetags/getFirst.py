from django.template import Library
import datetime

register = Library()

@register.filter(expects_localtime=True)
def getFirst(data):
    return list(data.values())[0]