from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("search-acc/", views.searchAcc, name="searchAcc")

]
