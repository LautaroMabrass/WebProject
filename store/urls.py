from django.urls import path
from . import views
urlpatterns = [
    path('',views.store_view, name = 'store'),
    path('buy/',views.buy_everything, name='buy')
]