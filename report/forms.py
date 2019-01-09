import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from transaction.models import Transaction, Operation
from category.models import Category


class ReportGenerateForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      required=True)
    operation = forms.ModelChoiceField(queryset=Operation.objects.all(),
                                       required=True)
    date_range = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(ReportGenerateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Generate', 'generate'))
        self.helper.disable_csrf = True
        self.helper.form_method = 'get'
        self.helper.form_action = 'result'
