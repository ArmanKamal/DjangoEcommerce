from django.db import models

# Create your models here.
class AdminLogin(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=240)


class AdminRegister(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)