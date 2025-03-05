from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('store/',views.store_view, name = 'store'),
]