from django import forms
from .models import Participant


class ForRegistrationFormm(forms.ModelForm):
    
    class Meta:
        model = Participant
        fields = ['email']
