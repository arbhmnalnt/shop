from django.contrib import admin
from stock.models import Box
from .models import *
# Register your models here.

class SoldAdmin(admin.ModelAdmin):
    search_fields   = ('id',)

admin.site.register(Sold, SoldAdmin)