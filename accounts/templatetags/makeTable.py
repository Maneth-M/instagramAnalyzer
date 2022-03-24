from django.template import Library
import datetime

register = Library()

@register.filter(expects_localtime=True)
def makeTable(data):
    new = {}
    dic = dict(data)
    flo = 0
    fli = 0
    pst = 0
    for key, value in dic.items():
        nflo = int(value['followers']) - int(flo)
        nfli = int(value['following']) - (int(fli))
        npst = int(value['medias']) - int(pst)
        new[key] = {
            'followers': int(nflo),
            'following': int(nfli),
            'medias': int(npst),
            'cfollowers': value['followers'],
            'cfollowing': value['following'],
            'cmedias': value['medias']
        }
        flo = value['followers']
        fli = value['following']
        pst = value['medias']
    return new.items().__reversed__()