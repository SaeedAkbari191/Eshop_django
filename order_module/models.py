from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False, verbose_name='Is paid')
    payment_date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Cart')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    final_price = models.IntegerField(null=True, blank=True, verbose_name='Final Price')
    count = models.IntegerField(verbose_name='Count')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'
