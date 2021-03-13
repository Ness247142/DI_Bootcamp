from django.contrib.auth.forms import UserCreationForm #form provided for registration
from django.contrib.auth.models import User
# from django import forms

# SIGN UP
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]

    


