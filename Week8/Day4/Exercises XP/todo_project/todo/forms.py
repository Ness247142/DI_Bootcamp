from django import forms
from .models import User, Todo, Category


class Signin_form(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class Login_form(Signin_form):
    def validate_unique(self):
        pass


class Create_todo_form(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'details', 'deadline_date']


class Category_form(forms.Form):
    # categories = Category.objects.values()
    category = forms.ChoiceField(
        choices=(Category.objects.values_list('id', 'name')))
