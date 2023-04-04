from django.contrib import admin
from .models import Motes, Data

# Register your models here.

class MotesData(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'section', 'location']


class DataData(admin.ModelAdmin):
    list_display = ['id', 'mote', 'last_collection', 'total', 'collect_date']


admin.site.register(Motes, MotesData)
admin.site.register(Data, DataData)
