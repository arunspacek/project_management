from django import forms
from .models import Project, Task, Issue, Comment


class ProjectCreationForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['company', 'title', 'description', 'user', 'deadline', 'status', 'budget']


class TaskCreationForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'project', 'user', 'description', 'priority', 'status']


class IssueCreationForm(forms.ModelForm):
	class Meta:
		model = Issue
		fields = ['title', 'description', 'image', 'threat_level', 'deadline', 'project', 'task', 'submitted_by']
		widgets = {
			'deadline': forms.widgets.DateInput(attrs={'type': 'date'})
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['user', 'comment']
