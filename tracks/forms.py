from django.forms import ModelForm

from tracks.models import ApplicationRecord


class ApplicationRecordForm(ModelForm):
    class Meta:
        model = ApplicationRecord

    fields = ['pub_date', 'headline', 'content', 'reporter']
