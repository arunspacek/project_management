from django.urls import path
from . import views


app_name = 'projects'

urlpatterns = [
	path('', views.project_list, name='project_list'),
	path('<int:project_id>', views.project_detail, name='project_detail'),
	path('<int:project_id>/tasks/', views.task_list, name='task_list'),
	path('<int:project_id>/tasks/<int:task_id>', views.task_detail, name='task_detail'),
	path('create_project/', views.create_project, name='create_project'),
	path('create_task/', views.create_task, name='create_task'),
	path('create_issue/', views.create_issue, name='create_issue'),
	path('issues/', views.issue_list, name='issue_list'),
	path('issues/<int:issue_id>', views.issue_detail, name='issue_detail'),
	]
