from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.models import ModelForm

from category.models import Category


class CategoryCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Category
        exclude = ('author',)
