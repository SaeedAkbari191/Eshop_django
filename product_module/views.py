from lib2to3.fixes.fix_input import context

from django.db.models import Count
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory, ProductBrand


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        brand_name = self.kwargs.get('brand')
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)
        return query


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_module/product_details.html'
    context_object_name = 'products'

    # def get_queryset(self):
    #     query = super(ProductDetailView, self).get_queryset()
    #     query = query.filter(is_active=True)
    #     return query


def category_partial(request):
    product_main_category = ProductCategory.objects.prefetch_related('productcategory_set').filter(is_active=True,
                                                                                                   parent_id=None)
    context = {
        'main_categories': product_main_category
    }
    return render(request, 'product_module/components/products_category_component.html', context)


def product_brand_component(request):
    product_brand = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brand
    }
    return render(request, 'product_module/components/product_brand_component.html', context)
