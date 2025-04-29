from itertools import product

from django.http import HttpResponse
from django.shortcuts import render

from product_module.models import Product


# Create your views here.
def add_to_order(request):
    print(request.GET)
    product_id = request.GET.get('product_id')
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        if product is not None:
            return HttpResponse('done')
    else:
        return HttpResponse('not auth')
