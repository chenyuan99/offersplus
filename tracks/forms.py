from django.forms import ModelForm

from tracks.models import ApplicationRecord


class ApplicationRecordForm(ModelForm):
    class Meta:
        model = ApplicationRecord
        fields = ['outcome', 'job_title', 'company_name', 'application_link']
