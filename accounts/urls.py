from django.urls import path, include

from . import views

urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    path('profile/', views.display_profile, name='profile'),
    path('register/', views.register, name='register')
]
