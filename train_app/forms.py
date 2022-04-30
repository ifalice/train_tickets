from django import forms
from django.core.validators import validate_email, MinLengthValidator
from .models import UserModels
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password
from .models import UserModels
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# from django.contrib.auth.password_validation import 

class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(max_length=40, validators=[MinLengthValidator(3)], help_text='Name>3<40')
 
    class Meta:
        model = UserModels
        fields = ['name', 'city', 'email', 'password1', 'password2', ]
        labels = {
            "name": "Name:",
            'city': 'City:',
            "password1": "Password:",
            "password2": "Password:",
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

    
    def clean_city(self):
        city = self.cleaned_data['city']
        for item in city:     
            if item.isdigit():
                raise forms.ValidationError('Pleace not digit')
        return city

    def clean_password1(self):
        password = self.cleaned_data['password1']
        # validate_password(password)
        errors = []
        digit = '1234567890'
        if len(password)<8:
            errors.append('<8')
        if not any(map(str.isdigit, password)):
            errors.append('not digit')
        if not any(map(str.isalpha, password)):
            errors.append('not alpha')
        if errors:
            raise forms.ValidationError(errors)
        return password   

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
       
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Not the same passwords'
            )
        return password2

class LoginUserForm(forms.ModelForm):

    class Meta:
        model = UserModels
        fields = ['name', 'password1']

        labels = {
            'name': 'Name:',
            'password1': 'Password:'
        }

        widgets = {
            'password1': forms.PasswordInput()
        }

    def clean_password1(self):
        name = self.cleaned_data.get('name')
        password = make_password(self.cleaned_data.get('password1'), salt='pbkdf2_sha256')
        user = UserModels.objects.get(name=name)
        
        if user.password1 != password:     
            raise forms.ValidationError('Invalid password or name')
        user.user_auth = 1
        user.save()
        return True
    