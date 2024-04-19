from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path("", views.display_companies, name="companies"),
    path(
        "view/<str:company_name>/",
        views.display_company,
        name="company-detail",
    ),
    path("grace-hopper", views.display_grace_hopper, name="grace-hopper"),
    path("internships", views.display_internships, name="internships"),
]
