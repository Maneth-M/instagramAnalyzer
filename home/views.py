from django.shortcuts import render, redirect, HttpResponse
from instagrapi import Client
from accounts.models import Account
from django.contrib import messages
import requests, datetime
from urllib.parse import quote
from projects.models import Project
cl = Client()
cl.login('butterbunny23', '123AgunamD')



def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            return redirect(f"/search-acc/?q={request.POST.get('q')}")
        accs = []
        for project in request.user.owner.all():
            for account in project.projectAccounts.all():
                accs.append(account)
        accs = list( dict.fromkeys(accs))
        return render(
            request,
            "home/index.html",
            {
                "accounts": accs
            }
        )

    else:
        return redirect('login')


# Quick Search Function
def searchAcc(request):
    request.META["Cross-Origin-Resource-Policy"] = "same-site"
    data = None
    if request.method == "GET":
        key = request.GET.get("q", "")

        if not Account.objects.filter(username=key.lower()).exists() and key != "":
            try:
                result = cl.user_info_by_username(key.lower()).dict()
                if result['is_private']:
                    messages.warning(request, "Sorry! We Can only Analyze Public Accounts")
                    return render(request, "home/search.html")
                else:
                    analyze = {
                        f"{datetime.datetime.now()}": {
                            'followers':result['follower_count'],
                            'following':result['following_count'],
                            'medias':result['media_count']
                        }
                    }
                    Account(
                        accountId=result['pk'],
                        username=result['username'],
                        profilePic=quote(result['profile_pic_url_hd']),
                        followers=result['follower_count'],
                        following=result['following_count'],
                        medias=result['media_count'],
                        analyze=analyze,
                        isVerified=result['is_verified'],
                        bio=result['biography']
                    ).save()
            except Exception as e:
                messages.error(request, "Something went wrong. Please Try again")
                return render(request, "home/search.html")
        data = Account.objects.filter(username=key.lower()).first()

    return render(
        request,
        "home/search.html",
        {
            "data": data
        }
    )


def hashtags(request):
    txt = request.GET.get("text", "")
    tags = []
    hard = []
    medium = []
    low = []
    if txt:
        txt = txt.split(" ")
        for tag in txt:
            print(tag)
            print(requests.get(f"https://www.instagram.com/explore/tags/{tag}/?__a=1").json())
    print(tags)
    return render(
        request,
        "home/hashtags.html",
        {
            "tags": tags
        }
    )