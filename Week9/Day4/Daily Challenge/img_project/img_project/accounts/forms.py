from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name",
                  "last_name", "password1", "password2"]

    password1 = forms.CharField(
        help_text='',
    )


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
