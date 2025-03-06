from django.urls import path

from . import views

app_name = 'shopping'

urlpatterns = [
    path('add/<int:product_id>', views.add_product, name = 'add'),
    path('less/<int:product_id>', views.less_product, name = 'less'),
    path('clean_product/', views.clean_product, name = 'clean'),
    path('delete/<int:product_id>', views.delete_product, name = 'delete')
]