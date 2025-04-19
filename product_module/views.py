from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory


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
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
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
    product_main_category = ProductCategory.objects.filter(is_active=True, parent_id=None).prefetch_related('productcategory_set')
    context = {
        'main_categories': product_main_category
    }
    return render(request, 'product_module/components/products_category_component.html', context)
