from django.urls import path
from . import views

app_name = 'companies'

urlpatterns = [
	path('', views.company_list, name='company_list'),
	path('<int:company_id>/', views.company_detail, name='company_detail'),
	path('create/', views.create_company, name='create_company'),
	]
