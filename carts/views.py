from django.shortcuts import render
from .models import Order
# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_completed=False)
        items = order.orderitem_set.all()
    else:
        items = []
        
    context={
        "items":items,
        'order': order
    }
    return render(request, 'carts/cart.html',context)

def checkout(request):
    context={}
    return render(request, 'carts/checkout.html',context)    