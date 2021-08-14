from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from products.models import Product
from carts.models import Order
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
        digital = request.POST.get("digital", False)
        image = request.FILES['image']
        product = Product.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price'],
            image = image,
            stock = request.POST['stock'],
            digital = digital
        )
        
    
        return redirect('/dashboard')
    else:
        return render(request,'product-create.html')

def edit(request,id):
    product = Product.objects.get(id=id)
    context = {"product":product}
    return render(request,"product-edit.html",context)

def update_product(request,id):
    product = Product.objects.get(id=id)
    context = {"product":product}
    if request.method == "POST":
        product = Product.objects.get(id=id)
        errors = Product.objects.validate_edit_product(request.POST)
        if errors:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(f'/dashboard/products/edit/{product.id}')
        digital = request.POST.get("digital", False)
        product.name = request.POST['name']
        product.description = request.POST['description']
        product.price = request.POST['price']
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.stock = request.POST['stock']
        product.digital = digital
        product.save()

        return redirect('/dashboard')
    return render(request,"product-edit.html",context)
        
        


def order_view(request):
    orders = Order.objects.all()
    context = {
        "orders": orders,
        
    }
    return render(request,'product-order.html',context)


def delete(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/dashboard')
