from django.http import JsonResponse
from django.shortcuts import render
from .generator import generate_response
# Create your views here.
def index(request):
    return render(request, 'jobgpt/jobgpt.html')


def get_prompt(request):
    if not request.user.is_authenticated:
        return JsonResponse({'prompt': 'You must be logged in to use this feature.'})
    result = generate_response(request.POST.get('prompt'))
    return JsonResponse({'prompt': result})
