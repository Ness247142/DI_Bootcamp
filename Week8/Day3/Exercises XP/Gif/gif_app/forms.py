from django import forms
from .models import *


class GifForm(forms.Form):
    title = forms.CharField(max_length=50)
    url = forms.URLField()
    uploader_name = forms.CharField(max_length=50)
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all())

    
class CategoryForm(forms.Form):
    name = forms.CharField(max_length=100)

    
