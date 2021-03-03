from django import forms

def check_old(age):
    if age > 65:
        raise forms.ValidationError(f'You are too old to be an astronaut')
        
def check_young(age):
    if age < 30:
        raise forms.ValidationError(f'You are not old enough to be an astronaut')

class AddAstroForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(
        label="",
        widget = forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            })
    )
    
    age = forms.IntegerField(
        validators=[check_old, check_young]
    )
    rank = forms.CharField(
        required=True,
        label="Type your Rank", 
        help_text='You better be in the military.', 
        error_messages={'required': 'Please enter a valid Rank'}
    )
    
