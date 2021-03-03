from django import forms


class TodoForm(forms.Form):
    title = forms.CharField(required=True)
    details = forms.CharField(required=True,
                              label="",
                              widget=forms.TextInput(
                                  attrs={
                                      'placeholder': 'Details',
                                      'class': 'form-control'
                                  })
                              )
    has_been_done = forms.BooleanField(required=False)
    date_creation = forms.DateTimeField()
    date_completion = forms.DateTimeField()
    deadline_date = forms.DateTimeField()
