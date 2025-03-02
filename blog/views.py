from django.shortcuts import render, redirect, HttpResponse
from .models import Category,Post


# Create your views here.
def blog_view(request):
    categories_all = Category.objects.all()
    post_all = Post.objects.all()
    return render(request, 'blog.html',{'categories_all' : categories_all, 'post_all' : post_all})