from django.shortcuts import render, redirect
from .models import Project
from accounts.models import Account
from django.contrib import messages
def projects(request):
    project = request.GET.get("project", "")
    add = request.GET.get("add", "")
    remove = request.GET.get("remove", "")

    if project:
        project = Project.objects.filter(projectId=project).first()
        if add:
            if project.projectAccounts.all().filter(accountId=add).exists():
                messages.info(request, "Account already added")
                redirect(f"/projects/?project={project.projectId}")
            else:
                project.projectAccounts.add(
                    Account.objects.filter(accountId=add).first()
                )
                project.save()
                messages.success(request, "Account added")
                redirect(f"/projects/?project={project.projectId}")
    else:
        project = Project.objects.first()
    if remove:
        acc = Account.objects.filter(accountId=remove).first()
        project.projectAccounts.remove(acc)
        project.save()
        messages.success(request, f"{acc.username} Removed")
    return render(
        request,
        "projects/projects.html",
        {
            "project": project
        }
    )