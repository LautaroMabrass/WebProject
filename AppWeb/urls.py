from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('store/',views.store_view, name = 'store'),
    path('blog/',views.blog_view, name = 'blog'),
    path('contact/',views.contact_view, name = 'contact')
]