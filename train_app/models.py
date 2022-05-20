from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.password_validation import MinimumLengthValidator

# Create your models here.


class TrainPaths(models.Model):
    short_train_path = models.CharField(max_length=100, default=None, null=True)
    long_train_path = models.TextField()


    def __str__(self):
        return f'{self.long_train_path}'



class TrainComposition(models.Model):
    name_of_train_car = models.CharField(max_length=100)
    train_car_composition = models.TextField()
    list_types_train_car = models.CharField(max_length=100, null=True, default=None)
    train_car_composition_json = models.JSONField(default=0)

    def __str__(self):
        return f'{self.name_of_train_car}'

class Train(models.Model):
    number_train = models.CharField(max_length=10)
    name_train = models.CharField(max_length=40, blank=True, null=True, default=None)
    train_composition = models.ForeignKey(TrainComposition, on_delete = models.CASCADE, null=True, default=None)

    def __str__(self):
        return f'{self.number_train}'


class TypeTrainCars(models.Model):
    type_train_car = models.CharField(max_length=100)
    number_of_seats = models.IntegerField()
    number_of_rows = models.IntegerField()
    place_size = models.CharField(max_length=100)
    all_number_seats = models.IntegerField(default=dict)

    def __str__(self):
        return f'{self.type_train_car}'
    
class City(models.Model):
    city_name = models.CharField(max_length=40)
    number_trains = models.ForeignKey(Train, on_delete = models.CASCADE, null=True, default=None, )
    train_paths = models.ForeignKey(TrainPaths, on_delete = models.CASCADE, null=True, default=None, )
    from_city_time = models.IntegerField()
    to_city_time = models.IntegerField(null=True, default=None, )

    def __str__(self):
        return f'{self.city_name} {self.from_city_time}'


class Tickets(models.Model):
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=100)
    train = models.ForeignKey(Train, on_delete = models.CASCADE, null=True, default=None )

