from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib import messages

from tracks.forms import ApplicationRecordForm
# Create your views here.
from tracks.models import ApplicationRecord


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    items = ApplicationRecord.objects.filter(applicant__username=request.user.username)
    for item in items: print((item.applicant.username, request.user.username))
    # myFilter = facultyFilter(request.GET, queryset=items)
    # items = myFilter.qs
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
    success_url = reverse_lazy('assessment:success')


class ApplicationRecordSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'tracks/success.html'


def edit_application(request, id):
    post = get_object_or_404(ApplicationRecord, id=id)

    # if request.method == 'GET':
    #     context = {'form': ApplicationRecordForm(instance=post), 'id': id}
    #     return render(request, 'blog/post_form.html', context)

    if request.method == 'GET':
        context = {'form': ApplicationRecordForm(instance=post), 'id': id}
        return render(request, 'tracks/application-record.html', context)

    elif request.method == 'POST':
        form = ApplicationRecordForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'tracks/application-record.html', {'form': form})


def hardware(request):
    return render(request, 'hardware.html')