from django.urls import path
from .views import LoginView, LogOutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='sing-in'),
    path('logout/', LogOutView.as_view(), name='sing-out'),
]
