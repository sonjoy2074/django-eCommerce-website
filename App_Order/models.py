from django.db import models
from django.conf import settings
from App_Shop.models import Product 
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    purchased = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.quantity} of {self.item}'
    
    def get_total(self):
        total = self.item.price * self.quantity
        float_total = format(total, '.2f')
        return float_total  # 100.00
    

class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    paymentId = models.CharField(max_length=100, blank=True, null=True)
    orderId = models.CharField(max_length=100, blank=True, null=True)

    def get_total(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total
    