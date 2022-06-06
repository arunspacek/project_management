from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Company
from .forms import CompanyRegistrationForm


def create_company(request):
	if request.method == "POST":
		form = CompanyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Company created successfully.")
	else:
		form = CompanyRegistrationForm()
		return render(request, 'companies/create_company.html', {'form': form})


def company_list(request):
	companies = Company.objects.all().order_by('-created')
	return render(request,'companies/list.html', {'companies': companies})


def company_detail(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	return render(request, 'companies/detail.html', {'company': company})
