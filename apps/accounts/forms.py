from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
