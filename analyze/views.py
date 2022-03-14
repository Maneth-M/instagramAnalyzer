from django.shortcuts import render
from projects.models import Project
# Create your views here.

def media (request):
    project = request.GET.get('project', "")
    if project:
        project = Project.objects.filter(projectId=project).first()
        accounts = project.projectAccounts.filter(media__datePosted__range=[""])