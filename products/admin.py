from django.contrib import admin
from .models import Category, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        )
        
    ordering = ('sku',) # ordering by sku in ascending order


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

