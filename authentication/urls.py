from django.urls import path
from .views import Vregister
urlpatterns = [
    path('',Vregister.as_view(), name = 'auth'),
]