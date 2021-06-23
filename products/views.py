from django.core.checks.messages import Error
from django.shortcuts import render
from ecommerce.utils import cookieCart
from .models import Product
# Create your views here.
def list(request):
    products = Product.objects.all()
    cookieData = cookieCart(request)
    context={"products":products}
    return render(request, 'products/list.html',context)



def detail(request,pk):
    product = Product.objects.get(id=pk)
    context = {
            "product": product
        }
    return render(request, "products/detail.html",context)
