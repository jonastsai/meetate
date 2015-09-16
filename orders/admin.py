from django.contrib import admin
from models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "create_at","output_at","user", "running_total", "status")

class ProductsAdmin(admin.ModelAdmin):
    list_display = ("green_coffee","create_at", "weight", "list_price")


class SellingItemsAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "selling_price")


# Register your models here.
admin.site.register(Orders, OrderAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(SellingItems, SellingItemsAdmin)
