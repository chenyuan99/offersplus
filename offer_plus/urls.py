from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tracks/', include('tracks.urls')),
    path('admin/', admin.site.urls),
]