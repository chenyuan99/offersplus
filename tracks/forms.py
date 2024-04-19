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
from django.forms import ModelForm

from tracks.models import ApplicationRecord


class ApplicationRecordForm(ModelForm):
    class Meta:
        model = ApplicationRecord
        fields = [
            "outcome",
            "job_title",
            "company_name",
            "application_link",
            "applicant",
        ]

    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput

        hide_condition = kwargs.pop("hide_condition", None)
        super(ApplicationRecordForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields["applicant"].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether.
