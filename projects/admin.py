from django.contrib import admin
from .models import Project, Task, Issue


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ['title', 'status']
	list_filter = ['created',]
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'status']
	list_filter = ['created', 'status']
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
	list_display = ['title', 'project', 'task']
	list_filter = ['created', 'deadline']
