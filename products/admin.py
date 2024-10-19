from django.contrib import admin
from .models import Products, Category

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )
    
admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
