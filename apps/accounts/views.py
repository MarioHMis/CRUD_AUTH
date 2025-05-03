from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'registration/registration/templates/registration/login.html'
    authentication_form = CustomLoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
