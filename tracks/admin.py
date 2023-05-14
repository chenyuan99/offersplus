from django.contrib import admin

# Register your models here.
from django.contrib import admin
from tracks.models import ApplicationRecord, Company

admin.site.register(ApplicationRecord)
admin.site.register(Company)