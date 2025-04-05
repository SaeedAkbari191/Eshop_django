from django.contrib import admin
from .models import Product, ProductCategory, ProductBrand, ProductTag


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'short_description', 'is_active']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
admin.site.register(ProductTag)
