from django.db import models
# from django.contrib.auth.password_validation import MinimumLengthValidator

# Create your models here.

class UserModels(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40, blank=True,)
    city = models.CharField(max_length=40, blank=True)
    email = models.EmailField(blank=True)
    password1 = models.CharField(max_length = 40)
    password2 = models.CharField(max_length = 40)
    super_user = models.BooleanField(blank=True, null=True)
    user_auth = models.BooleanField(blank=True, null=True)


    
