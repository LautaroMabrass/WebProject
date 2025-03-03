from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_view, name = 'blog'),
    path('category/<int:id_category>',views.blog_category, name='blog_categories')
]