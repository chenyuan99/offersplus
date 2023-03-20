from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('tracks.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
