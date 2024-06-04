from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# class MyForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["username","first_name"]
#         widgets = {
#             "username":forms.TextInput(attrs={"class":"input w100"})
#         }

class CustomLoginForm(AuthenticationForm):
    
    
    class Meta:
        model = User
        fields = ["username","password"]

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["email","first_name","password1","password2"]