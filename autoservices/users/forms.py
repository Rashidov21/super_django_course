from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from main.models import Service

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name',"username", 'last_name', "phone")
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.phone
        if commit:
            user.save()
        return user 

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    
# class ServiceCreateForm(forms.ModelForm):
    
#     class Meta:
#         model = Service
#         fields = "__all__"
#         exclude = ('user',)