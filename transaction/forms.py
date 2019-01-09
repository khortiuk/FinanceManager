from django.forms.models import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Transaction


class TransactionCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(TransactionCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('Create', 'Create'))

    class Meta:
        model = Transaction
        exclude = ('author', 'date')
