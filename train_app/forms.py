from django import forms
from django.core.validators import validate_email, MinLengthValidator
from .models import UserModels
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
# from django.contrib.auth.password_validation import 

class RegisterUserForm(forms.ModelForm):
    # name = forms.CharField(max_length=40, validators=[MinLengthValidator(3)], help_text='Name>3<40')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password:')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Password:')
    class Meta:
        
        model = User
        fields = ['username', 'email',]
        labels = {
            "username": "Name:",
            'email': 'Email address:'
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

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class LoginUserForm(forms.Form):
    username = forms.CharField(label='Login:', widget=forms.TextInput())
    password = forms.CharField(label='Password:', widget=forms.PasswordInput())

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:     
            raise forms.ValidationError('Invalid login or password')
        return password

class IndexPageForm(forms.Form):
    from_city = forms.CharField(label='From city:')
    to_city = forms.CharField(label='To city')
    data = forms.DateField(label='Data')