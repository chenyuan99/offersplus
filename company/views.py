import logging
import urllib.request, json
from collections import defaultdict

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Add these imports at the top of your View file
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

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


def display_internships(request):
    context = defaultdict()
    items = list()
    with urllib.request.urlopen(
            "https://raw.githubusercontent.com/SimplifyJobs/Summer2024-Internships/dev/.github/scripts/listings.json") as url:
        data = json.loads(url.read().decode('utf-8'))
        for item in data:
            try:
                # logging.info(item)
                items.append(item)
            except:
                logging.warning("An exception occurred")
    # context['internships'] = internships
    # Paginate items

    # Get page number from request,
    # default to first page
    default_page = 1
    page = request.GET.get('page', default_page)

    items_per_page = 100
    paginator = Paginator(items, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    # Provide filtered, paginated library items
    context["items_page"] = items_page

    return render(request, 'company/internships.html', context)


def display_newgrads(request):
    with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
        data = json.load(url)
        print(data)
    return render(request, 'company/grace-hopper.html')
