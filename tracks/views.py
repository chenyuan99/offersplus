import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib import messages

from tracks.forms import ApplicationRecordForm
# Create your views here.
from tracks.models import ApplicationRecord, Company


def report_statistics(items: QuerySet[ApplicationRecord]):
    """
    Displays statistics about the job applications
    :param items: QuerySet of ApplicationRecord objects
    :return: a dictionary with the statistics of applications
    """
    rejected = ApplicationRecord.objects.filter(outcome__contains="REJECT").count()
    oa = ApplicationRecord.objects.filter(outcome="OA").count()
    vo = ApplicationRecord.objects.filter(outcome="VO").count()
    statistics = {
        'oa': oa,
        'rejected': rejected,
        'vo': vo
    }
    return statistics


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    items = ApplicationRecord.objects.filter(applicant__username=request.user.username)
    # for item in items: print((item.applicant.username, request.user.username))
    # myFilter = facultyFilter(request.GET, queryset=items)
    # items = myFilter.qs
    statistics = report_statistics(items)
    logging.info(statistics)
    context = {
        'items': items,
        # 'header': 'faculty',
        # 'myFilter': myFilter,
    }
    return render(request, 'index.html', context)


# Pre Post Form related view
class ApplicationRecordView(LoginRequiredMixin, FormView):
    template_name = 'tracks/application-record.html'
    form_class = ApplicationRecordForm
    success_url = reverse_lazy('tracks:success')


class ApplicationRecordSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'tracks/success.html'


def edit_application(request, id):
    post = get_object_or_404(ApplicationRecord, id=id)

    if request.method == 'GET':
        context = {'form': ApplicationRecordForm(instance=post), 'id': id}
        return render(request, 'tracks/application-record.html', context)

    if request.method == 'POST':
        form = ApplicationRecordForm(request.POST, instance=post)
        if form.is_valid():
            form.applicant = request.user.username
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'tracks/application-record.html', {'form': form})


def hardware(request):
    return render(request, 'hardware.html')


# -------------------------add-----------------------------------
def add_application(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    if request.method == 'POST':
        form = ApplicationRecordForm(request.POST, hide_condition=True)

        if form.is_valid():
            form.applicant = request.user.username
            logging.info(form)
            form.save()
            return redirect('index')

    else:
        form = ApplicationRecordForm(hide_condition=True)
        form.initial['applicant'] = request.user.username
        return render(request, 'add_new.html', {'form': form})


def companies(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'companies.html', context)


def yuanc(request):
    companies = Company.objects.all()
    context = {"companies": companies}
    return render(request, 'yuanc.html', context)
