from django.contrib.auth import authenticate, login
from django.views import generic
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.contrib.auth.views import LogoutView
from .froms import UserLoginFrom


class LoginView(generic.FormView):
    form_class = UserLoginFrom
    template_name = 'user_profile/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super(LoginView, self).get(request, *args, **kwargs)

    @never_cache
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        self.success_url = self.request.GET.get('next') or '/'
        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(LogoutView):

    def get(self, request, *args, **kwargs):
        self.next_page = self.request.GET.get('next') or '/'
        super(LogOutView, self).get(request, *args, **kwargs)
