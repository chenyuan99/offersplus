from django.urls import path

from . import views

urlpatterns = [
    path('logout', views.logout_request, name='logout'),
    path('register/', views.register, name='register')
]
