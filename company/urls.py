from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.display_companies, name='companies'),
    path('view/<str:company_name>/', views.display_company, name='company-detail'),
]
