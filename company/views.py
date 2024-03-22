import logging

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from tracks.models import Company, ApplicationRecord


def display_companies(request):
    items = Company.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'company/company.html', context)


def display_company(request, company_name):
    if not request.user.is_authenticated:
        return redirect('login')
    logging.info(company_name)
    items = ApplicationRecord.objects.filter(company_name=company_name, applicant=request.user.username)
    context = {
        'items': items,
        'company': company_name
    }
    return render(request, 'company/company-detail.html', context)


def display_grace_hopper(request):
    return render(request, 'company/grace-hopper.html')