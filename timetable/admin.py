from django.contrib import admin
from .models import Ferry, Port

# Register your models here.

# admin.site.register(Ferry, Port) или так
@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Ferry)
class FerryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "date",
        "time_departure",
        "port_departure",
        "time_arrival",
        "port_arrival",
    ]
