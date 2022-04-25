from django.db import models

# Create your models here.

class UserModels(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40, blank=True)
    city = models.CharField(max_length=40, blank=True)
    email = models.EmailField()
    password1 = models.CharField(max_length = 40)
    password2 = models.CharField(max_length = 40)
    super_user = models.BooleanField()
    user_auth = models.BooleanField()


    
