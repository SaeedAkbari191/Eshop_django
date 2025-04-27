from django.db.models import Count
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from utils.http_service import get_client_ip
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = 'product_module/product_list.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 5

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('category')
        brand_name = self.kwargs.get('brand')
        request = self.request
        start_price = request.GET.get('start_price')
        if start_price is not None:
            query = query.filter(price__gte=start_price)
        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)
        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)
        return query


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_module/product_details.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        load_product = self.object
        request = self.request
        favorite_product_id = request.session.get('ProductFavorite')
        context['is_favorite'] = favorite_product_id == str(load_product.id)
        context['product_galleries'] = ProductGallery.objects.filter(product_id=load_product.id).all()
        context['related_products'] = Product.objects.filter(brand_id=load_product.brand_id).exclude(
            pk=load_product.id).all()[:12]

        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user
        has_benn_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=load_product.id).exists()
        if not has_benn_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=load_product.id)
            new_visit.save()
        return context


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
