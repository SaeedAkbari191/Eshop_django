from django.contrib import admin
from .models import Product, ProductCategory, ProductBrand, ProductTag, ProductVisit, ProductGallery


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'brand', 'price', 'short_description', 'is_active']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'is_active']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductBrand)
admin.site.register(ProductTag)
admin.site.register(ProductVisit)
admin.site.register(ProductGallery)
