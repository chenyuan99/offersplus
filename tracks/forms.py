from django.forms import ModelForm

from tracks.models import ApplicationRecord


class ApplicationRecordForm(ModelForm):
    class Meta:
        model = ApplicationRecord
        fields = ['outcome', 'job_title', 'company_name', 'application_link','applicant']

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition', None)
        super(ApplicationRecordForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['applicant'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.