from django import forms
from .models import Service


class ServiceCreateForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ('user',)