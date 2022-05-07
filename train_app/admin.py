from django.contrib import admin
from .models import City, Train, TrainPaths
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'from_city_time','number_trains', 'train_paths']
    # filter_horizontal = ['train_path_id', 'number_train']
    search_fields = ['city_name']
    

admin.site.register(City, CityAdmin)
admin.site.register(Train)
admin.site.register(TrainPaths)