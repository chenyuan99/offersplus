from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-application', views.ApplicationRecordView.as_view(), name='add-application'),
    path('application/edit/<int:id>/', views.edit_application, name='application-edit'),
]
