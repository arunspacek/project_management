from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'website']
	list_filter = ['location', 'created']
	prepopulated_fields = {'slug': ('name',)}
