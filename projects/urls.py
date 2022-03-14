from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.projects, name="projects"),
    path("analyze", include("analyze.urls"))
]
