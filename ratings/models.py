from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(blank=True,null=True)
    subject = models.CharField(max_length=50,blank=True,null=True)
    rating = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
