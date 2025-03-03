from django.shortcuts import render, redirect, HttpResponse
from .models import Category,Post


# Create your views here.
def blog_view(request):
    categories_all = Category.objects.all().distinct()
    post_all = Post.objects.all()
    return render(request, 'blog.html',{'categories_all' : categories_all, 'post_all' : post_all})

def blog_category(request, id_category):
    category_filter = Category.objects.get(id=id_category)
    post_filter = Post.objects.filter(category = category_filter)
    categories__all = Category.objects.all().distinct()
    return render(request, 'category_filter.html',{"categories_all" : category_filter, "post_all": post_filter, "categories__all" : categories__all})