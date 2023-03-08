from django.contrib import admin

from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'category',
    ]
    list_filter = ['name', 'category']
    search_fields = ['name', 'category']
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category, CategoryAdmin)