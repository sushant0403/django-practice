from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count

# Create your models here.


class Product(models.Model):
    name                = models.CharField(max_length=200,blank = True, null= True)
    image               = models.ImageField(upload_to='static/images', blank = True, null= True)
    description         = models.TextField(blank = True, null= True)
    created_at          = models.DateTimeField(auto_now=True)
    updated_at          = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def averagereview(self):
        reviews = Comment.objects.filter(product=self).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(product=self).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

class Comment(models.Model):
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    rating              = models.FloatField(blank = True,null=True)
    comment             = models.CharField(max_length=100, blank = True)
    created_date        = models.DateTimeField(auto_now_add=True)
    updated_date        = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name  + ". User : " + self.user.username
