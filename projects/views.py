from django.shortcuts import render
from .models import Project

def projects(request):
    project = request.GET.get("project", "")
    if project:
        project = Project.objects.filter(projectId=project).first()
    else:
        project = Project.objects.first()
    return render(
        request,
        "projects/projects.html",
        {
            "project": project
        }
    )