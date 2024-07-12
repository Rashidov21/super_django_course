from django import forms
from .models import Service
from users.models import CustomUser


class ServiceCreateForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = "__all__"
        exclude = ('user',)
        widgets = {
            'work_time_start': forms.TimeInput(attrs={'type': 'time'}),
            'work_time_end': forms.TimeInput(attrs={'type': 'time'}),
            'working_days': forms.CheckboxSelectMultiple(),
        }
        
    def save(self, commit=True):
        service = super().save(commit=False)
        if commit:
            service.save()
        return service