from django.db import models

from account_module.models import User
from product_module.models import Product


# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')
    is_paid = models.BooleanField(default=False, verbose_name='Is paid')
    payment_date = models.DateField(blank=True, null=True, verbose_name='Payment date')

    def __str__(self):
        return str(self.user)

    def calculate_total_price(self):
        total_amount: int = 0
        if self.is_paid:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.final_price * order_detail.count
        else:
            for order_detail in self.orderdetail_set.all():
                total_amount += order_detail.product.price * order_detail.count

        return total_amount

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

    def total_price(self):
        return self.count * self.product.price

    class Meta:
        verbose_name = 'Order Detail'
        verbose_name_plural = 'Order Details'
