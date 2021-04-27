from django.shortcuts import render
from ecommerce.utils import cookieCart
from .models import Product
# Create your views here.
def list(request):
    products = Product.objects.all()
    cookieData = cookieCart(request)
    context={"products":products}
    return render(request, 'products/list.html',context)



