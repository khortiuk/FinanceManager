from django import forms
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, ButtonHolder

from user_profile.models import UserProfile


class UserLoginFrom(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginFrom, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )
