from django.shortcuts import render
from .models import Product
# Create your views here.
def list(request):
    products = Product.objects.all()
    context={"products":products}
    return render(request, 'products/list.html',context)



