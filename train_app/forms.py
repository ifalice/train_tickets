from django.forms import ModelForm
from .models import UserModels


class RegisterUserForm(ModelForm):
    class Meta:
        model = UserModels
        fields = ['name', 'password1', 'password2']
        labels = {
            "name": "Name",
            "password1": "Password",
            "password2": "Password",
        }
        
        

