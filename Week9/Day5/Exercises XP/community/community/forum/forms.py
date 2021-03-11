from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['released_date']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'textarea'}),
            'author': forms.Select(attrs={'class': 'select'})
        }
