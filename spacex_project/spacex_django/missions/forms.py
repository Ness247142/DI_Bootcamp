from django import forms
from .models import Mission, Rocket

        
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
        validators=[check_young]
    )
    rank = forms.CharField(
        required=True,
        label="Type your Rank", 
        help_text='You better be in the military.', 
        error_messages={'required': 'Please enter a valid Rank'}
    )
    


class AddMissionForm(forms.ModelForm):
    class Meta:      
        model = Mission
        fields = '__all__'



class AddRocketForm(forms.ModelForm):
    class Meta:      
        model = Rocket
        fields = '__all__'

    