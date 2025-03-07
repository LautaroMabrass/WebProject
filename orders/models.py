from django.db import models
from django.contrib.auth import get_user_model
from store.models import products
from django.db.models import F, Sum, FloatField

User = get_user_model()

class orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"
    
    @property
    def total(self):
        return self.allOrders_set.aggregate(
            total=Sum(F('product_id__price') * F('amount'), output_field=FloatField())
        )['total']

class allOrders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)
    order_id = models.ForeignKey(orders, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.amount} -> {self.product_id.name}'
