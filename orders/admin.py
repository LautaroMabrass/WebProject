from django.contrib import admin
from .models import orders, allOrders
# Register your models here.

admin.site.register([orders,allOrders])