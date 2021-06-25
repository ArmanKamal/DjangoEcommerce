from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from products.models import Product
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "products":Product.objects.all().order_by('created_at')
    }
    return render(request, "home.html",context)

def create(request):
    if request.method == "POST":
        errors = Product.objects.validate_product(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/dashboard/products/create')
  
        product = Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price'],
            image = request.POST['image'],
            stock = request.POST['stock'],
        
        )
    
    
        return redirect('/dashboard')
    else:
        return render(request,'product-create.html')
