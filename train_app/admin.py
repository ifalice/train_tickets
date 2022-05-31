from django.contrib import admin
from .models import City, Train, TrainPaths, TypeTrainCars, TrainComposition, Tickets
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'from_city_time','to_city_time','number_trains', 'train_paths']
    # filter_horizontal = ['train_path_id', 'number_train']
    search_fields = ['city_name']


class TicketsAdmin(admin.ModelAdmin):
    list_display = ['name_passenger', 'surname_passenger', 'number_train', 'number_train_car', 'number_seats']

admin.site.register(City, CityAdmin)
admin.site.register(Train)
admin.site.register(TrainPaths)
admin.site.register(TypeTrainCars)
admin.site.register(TrainComposition)
admin.site.register(Tickets, TicketsAdmin)
