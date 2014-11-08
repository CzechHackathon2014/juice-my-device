from django.contrib import admin

# Register your models here.
from .models import Place

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'venue_uid')

admin.site.register(Place, PlaceAdmin)