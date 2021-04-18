from django.shortcuts import render

# Create your views here.
def cart(request):
    context={}
    return render(request, 'carts/cart.html',context)

def checkout(request):
    context={}
    return render(request, 'carts/checkout.html',context)    