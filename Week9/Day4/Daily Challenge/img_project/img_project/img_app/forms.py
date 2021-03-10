from django import forms
from .models import *


class AddImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        ordering = ('id')
