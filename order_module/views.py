from itertools import product

from django.http import HttpResponse
from django.shortcuts import render

from product_module.models import Product


# Create your views here.
def add_to_order(request):
    product_id = request.GET.get('product_id')
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_deleted=False).first()
        if product is not None:
            return HttpResponse('done')
    else:
        return HttpResponse('not auth')
