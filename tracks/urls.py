from django.template.defaulttags import url
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hardware", views.hardware, name="hardware"),
    path("yuanc", views.yuanc, name="yuanc"),
    path("companies", views.companies, name="companies"),
    path("add-application", views.add_application, name="add-application"),
    path(
        "application/edit/<int:id>/",
        views.edit_application,
        name="application-edit",
    ),
    # url(r'^add_device$', views.add_application),
]
