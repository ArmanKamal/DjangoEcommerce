from django.db import models
from django.contrib.auth.models import User
import re
POSITIVE_REGEX = re.compile(r"/^[+]?([0-9]+(?:[\.][0-9]*)?|\.[0-9]+)$/")
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=120,null=True,blank=True)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class ProductManager(models.Manager):
 
    def validate_product(self,postData):
        errors = {}
        if len(postData['name'])<=0:
            errors['p_name'] = "Product name cannot be empty"
        if len(postData['price']) <= 0:
            errors['p_p_empty'] = "Price cannot be empty"
        if postData['price']<='0':
                errors['p_price'] = "Price cannot be negative"
        if len(postData['description']) <=0 :
            errors['description'] = "Description cannot be empty"
        return errors
    
   
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(null=True,blank=True,upload_to ='images/')
    stock = models.IntegerField(null=True,blank=True)
    description = models.TextField(default="No description found")
    digital = models.BooleanField(default=False,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
    def __str__(self):
        return self.name

