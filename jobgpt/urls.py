from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='jobgpt'),
    path('prompt', views.get_prompt, name='prompt'),
]
