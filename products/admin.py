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
        'is_weekly_bargain',
    )
    list_editable = ('is_weekly_bargain',) 
    ordering = ('sku',)

    def save_model(self, request, obj, form, change):
        # Ensure only one product is marked as the weekly bargain
        if obj.is_weekly_bargain:
            Products.objects.filter(is_weekly_bargain=True).update(is_weekly_bargain=False)
        super().save_model(request, obj, form, change)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )
    
admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
