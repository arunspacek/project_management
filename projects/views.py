from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Project, Task, Issue
from .forms import ProjectCreationForm, TaskCreationForm, IssueCreationForm


def project_list(request):
	projects = Project.objects.all()
	return render(request, "projects/list.html", {'projects': projects})


def project_detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, "projects/detail.html", {'project': project})


def task_list(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	tasks = Task.objects.filter(project=project)
	return render(request, "projects/task_list.html", {"project": project, "tasks": tasks})


def task_detail(request, project_id, task_id):
	project = get_object_or_404(Project, id=project_id)
	task = get_object_or_404(Task, project=project, pk=task_id)
	return render(request, "projects/task_detail.html", {"project": project, "task": task})


def create_project(request):
	if request.method == "POST":
		form = ProjectCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Project creation successful.")
		else:
			return HttpResponse("The form is invalid.")
	else:
		form = ProjectCreationForm()
		return render(request, 'projects/create_project.html', {'form': form})


def create_task(request):
	if request.method == "POST":
		form = TaskCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Task creation successful.")
	else:
		form = TaskCreationForm()
		return render(request, 'projects/create_task.html', {'form': form})


def create_issue(request):
	if request.method == "POST":
		form = IssueCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Issue submitted successfully.")
		else:
			return render(request, "projects/invalid_form.html", {"form": form})
	else:
		form = IssueCreationForm()
		return render(request, 'projects/create_issue.html', {'form': form})


def issue_list(request):
	issues = Issue.objects.all()
	return render(request, 'projects/issue_list.html', {'issues': issues})


def issue_detail(request, issue_id):
	issue = get_object_or_404(Issue, pk=issue_id)
	return render(request, 'projects/issue_detail.html', {'issue': issue})
