from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class Registration(UserCreationForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]

class LoginForm(AuthenticationForm):
    pass