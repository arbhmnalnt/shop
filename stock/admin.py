from django.contrib import admin
from .models import Box
# Register your models here.

class BoxAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'amount')
    search_fields   = ('id', 'name')

admin.site.register(Box, BoxAdmin)