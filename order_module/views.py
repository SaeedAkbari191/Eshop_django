from itertools import product

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from order_module.models import Order, OrderDetail
from product_module.models import Product


# Create your views here.
def add_to_order(request):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))

    if count < 1:
        return JsonResponse({
            'status': 'Invalid Count.',
            'text': 'Invalid Count.',
            'confirmButtonText': 'Ok!'
        })
    if request.user.is_authenticated:
        product = Product.objects.filter(id=product_id, is_active=True, is_deleted=False).first()
        if product is not None:
            current_order, created = Order.objects.get_or_create(is_paid=False, user=request.user)
            current_order_details = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_details is not None:
                print('details')
                current_order_details.count += count
                current_order_details.save()
            else:
                new_details = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_details.save()
            return JsonResponse({
                'status': 'SUCCESS',
                'text': 'The Product has been successfully added. to your shopping cart',
                'confirmButtonText': 'Ok!'
            })

        else:
            return JsonResponse({
                'status': 'Not Found',
                'text': 'Invalid Count.',
                'confirmButtonText': 'Ok!'
            })
    else:
        return JsonResponse({
            'status': 'Not Authorized',
            'text': 'Invalid Count.',
            'confirmButtonText': 'Ok!'
        })
