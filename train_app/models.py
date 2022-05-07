from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import MinimumLengthValidator

# Create your models here.

# class UserModels(models.Model):
#     name = models.CharField(max_length=40)
#     surname = models.CharField(max_length=40, blank=True,)
#     city = models.CharField(max_length=40, blank=True)
#     email = models.EmailField(blank=True)
#     password1 = models.CharField(max_length = 40)
#     password2 = models.CharField(max_length = 40)
#     super_user = models.BooleanField(blank=True, null=True)
#     user_auth = models.BooleanField(blank=True, null=True)


class TrainPaths(models.Model):
    short_train_path = models.CharField(max_length=100, default=None, null=True)
    long_train_path = models.TextField()


    def __str__(self):
        return f'{self.long_train_path}'


class Train(models.Model):
    number_train = models.CharField(max_length=10)
    name_train = models.CharField(max_length=40, blank=True, null=True, default=None)

    def __str__(self):
        if self.name_train:
            return f'{self.number_train} {self.name_train}'
        return f'{self.number_train}'
    
class City(models.Model):
    city_name = models.CharField(max_length=40)
    number_trains = models.ForeignKey(Train, on_delete = models.CASCADE, null=True, default=None, )
    train_paths = models.ForeignKey(TrainPaths, on_delete = models.CASCADE, null=True, default=None, )
    from_city_time = models.IntegerField()
    to_city_time = models.IntegerField(null=True, default=None, )

    def __str__(self):
        return f'{self.city_name} {self.from_city_time}'