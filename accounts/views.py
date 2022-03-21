from django.shortcuts import render
from .models import Account

def account(request):
    acc = request.GET.get("account", "")
    if Account.objects.filter(accountId=acc).exists():
        account = Account.objects.filter(accountId=acc).first()
    else:
        account = ""
    return render(
        request,
        "accounts/account.html",
        {
            'account': account
        }
    )
