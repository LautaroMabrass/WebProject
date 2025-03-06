from django.contrib import admin
from .models import categoryProduct, products

# Register your models here.

class categoryProdAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class productAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


admin.site.register(categoryProduct, categoryProdAdmin)
admin.site.register(products, productAdmin)