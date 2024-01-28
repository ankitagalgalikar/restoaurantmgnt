from django.contrib import admin
from Restoapp.models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','detail','cat','is_active']
    list_filter=['cat','is_active']
admin.site.register(Product,ProductAdmin)

