from django import forms

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Field, Fieldset, Layout, Submit

from .models import Organization


class OrganizationForm(forms.ModelForm):

    class Meta:

        model = Organization
        fields = ['name', 'description', ]

    def __init__(self, *args, **kwargs):
        super(OrganizationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout()
        self.helper.add_layout(
            FormActions(Submit('submit', 'Submit', css_class='button button--primary')),
        )
