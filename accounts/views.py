from django.shortcuts import render
from .models import Account, Media
from django.db.models import Max


def account(request):
    acc = request.GET.get("account", "")
    sort = request.GET.get("sort", "")
    if Account.objects.filter(accountId=acc).exists():
        account = Account.objects.filter(accountId=acc).first()
    else:
        account = ""

    if sort == "" or sort == "L":
        medias = Media.objects.filter(account=account).all().annotate(Max("likes")).order_by('-likes__max')
    elif sort == "C":
        medias = Media.objects.filter(account=account).all().annotate(Max("comments")).order_by('-comments__max')
    else:
        medias = Media.objects.filter(account=account).all().annotate(Max("views")).order_by('-views__max')

    return render(
        request,
        "accounts/account.html",
        {
            'account': account,
            'medias': medias
        }
    )
