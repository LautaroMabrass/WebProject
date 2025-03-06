from django.db import models

# Create your models here.

class categoryProduct(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to='store')
    diponibility = models.BooleanField(default=True)
    category =  models.ForeignKey(categoryProduct, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name