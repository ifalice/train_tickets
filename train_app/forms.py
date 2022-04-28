from django import forms
from django.core.validators import validate_email, MinLengthValidator
from .models import UserModels
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password
# from django.contrib.auth.password_validation import 

class RegisterUserForm(forms.ModelForm):
    name = forms.CharField(max_length=40, validators=[MinLengthValidator(3)], help_text='Name>3<40')
 
    class Meta:
        model = UserModels
        fields = ['name', 'city', 'email', 'password1', 'password2', ]
        labels = {
            "name": "Name",
            'city': 'City',
            "password1": "Password",
            "password2": "Password",
        }
        widgets = {
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

     
    # def clean(self):
    #         password1 = self.cleaned_data.get('password1')
    #         password2 = self.cleaned_data.get('password2')
    #         if password1 != password2:
    #             self.add_error('password1', 'Not the same passwords ')

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
            salt = 'hi'
            hash_password = make_password(password)
            check_pass = check_password(password, hash_password)
            errors.append(hash_password)
            errors.append(check_pass)
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


               
    # def clean_password1(self, *args, **kwargs):
    #         cleaned_data = super(RegisterUserForm, self).clean()
    #         password = cleaned_data.get('password1')
    #         if '1' in password:
    #             return password
    #         raise forms.ValidationError(cleaned_data)    

    
    
    # def clean_password2(self, *args, **kwargs):
    #         password = self.cleaned_data
    #         password_2 = self.cleaned_data.get('password2')
    #         a = [password, password_2]
    #         if not password:
    #             return password
    #         raise forms.ValidationError(f'{password}')  

    
