# Copyright Yuan Chen. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://www.yuanchen.io/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

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
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field="username",
        default="cyuan8",
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return " ".join([self.job_title, self.company_name, self.outcome])


class Company(models.Model):
    name = models.TextField()
    industry = models.TextField(blank=True)
    logo = models.ImageField(upload_to="company_logo", blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.name
