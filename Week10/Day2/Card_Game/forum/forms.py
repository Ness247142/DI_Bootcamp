from django import forms
from .models import *
from django.contrib.auth.models import User

class ThreadInputForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = [
            'headline',
            'subject',
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]