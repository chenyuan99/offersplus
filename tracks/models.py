from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ApplicationRecord(models.Model):
    outcome = models.TextField(blank=True)
    job_title = models.TextField(blank=True)
    company_name = models.TextField()
    application_link = models.TextField(blank=True)
    OA_date = models.DateTimeField(null=True,blank=True)
    VO_date = models.DateTimeField(null=True,blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return " ".join([self.job_title,self.company_name, self.outcome])
