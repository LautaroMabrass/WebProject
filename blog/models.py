from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog', null = True, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title