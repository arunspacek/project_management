from django import forms
from .models import Company


class CompanyRegistrationForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ['name', 'email', 'website', 'location', 'about']
