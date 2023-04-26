from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


@login_required
def project_list(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }

    return render(request, "projects/list.html", context)


@login_required
def show_projects(request, id):
    project = Project.objects.get(id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)
