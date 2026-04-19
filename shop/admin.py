from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)


class StockAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'inventory', 'available', 'created', 'updated']
    list_editable = ['price', 'inventory', 'available']
    list_per_page = 15

admin.site.register(Stock, StockAdmin) 
