from django.db import models
from django.contrib.auth.models import User
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


class TrainPath(models.Model):
    train_path = models.TextField()


class Train(models.Model):
    number_train = models.CharField(max_length=10)
    name_train = models.CharField(max_length=40, blank=True)
    
class City(models.Model):
    city_name = models.CharField(max_length=40)
    number_train = models.ManyToManyField(Train)
    train_path_id = models.ManyToManyField(TrainPath)
    from_city_time = models.CharField(max_length=10)
    to_city_time = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.city_name, self.number_train, self.train_path_id, self.from_city_time, self.to_city_time,}'