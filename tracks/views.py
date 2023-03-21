from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from tracks.models import ApplicationRecord


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    items = ApplicationRecord.objects.filter(applicant__username=request.user.username)
    for item in items: print((item.applicant.username,request.user.username))
    # myFilter = facultyFilter(request.GET, queryset=items)
    # items = myFilter.qs
    context = {
        'items': items,
        # 'header': 'faculty',
        # 'myFilter': myFilter,
    }
    return render(request, 'index.html', context)
