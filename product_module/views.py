from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_list.html'
    context_object_name = 'products'

    # def get_queryset(self):
    #     base_query = super(ProductListView, self).get_queryset()
    #     data = base_query.filter(is_active=True)
    #     return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_module/product_details.html'
    context_object_name = 'products'
