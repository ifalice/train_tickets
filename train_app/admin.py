from django.contrib import admin

# Register your models here.

class CityAdmin(admin.ModelAdmin):
    fields = ['city_name', 'from_city_time', 'to_city_time']