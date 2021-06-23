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
        if len(errors) >= 0:
            messages.error(request,errors)
            return redirect('/dashboard/products/create')
        Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price'],
            digital = request.POST['digital'],
            image = request.POST['image'],
            stock = request.POST['stock']
        
        )
        return redirect('/dashboard')

    return render(request,'product-create.html')
