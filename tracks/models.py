from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.
from tracks.identifiers import MY_CHOICES


class ApplicationRecord(models.Model):
    outcome = models.TextField(choices=MY_CHOICES)
    job_title = models.TextField(blank=True)
    company_name = models.TextField()
    application_link = models.TextField(blank=True)
    OA_date = models.DateTimeField(null=True, blank=True)
    VO_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, to_field='username', default='cyuan8',
                                  on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return " ".join([self.job_title, self.company_name, self.outcome])
