from typing import Any
from django import forms 
from .models import Players


class DateInput(forms.DateInput):
    input_type = 'date'

class AdPlayerForm(forms.ModelForm):
    # write your inputs here 
    dr = forms.DateField(widget=DateInput)
    class Meta:
        model = Players
        fields = "__all__"
        exclude = ['number','age']
        
        widgets = {
            'dr':forms.DateInput()
        }