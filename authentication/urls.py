from django.urls import path
from .views import Vregister
from .views import view_close, close_sesion, login_view
urlpatterns = [
    path('',Vregister.as_view(), name = 'auth'),
    path('logout/',view_close, name = 'logout'),
    path('end/', close_sesion, name = 'end'),
    path('login/', login_view, name = 'login_')
]