from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
import datetime
from .models import Order,OrderItem,Product,Shipping
from django.contrib import messages
from ecommerce.utils import cookieCart
# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_completed=False)
        items = order.orderitem_set.all()

    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        items = cookieData['items']
            
        

    context={
        "items":items,
        'order': order,
    }
    return render(request, 'carts/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, order_completed=False)
        items = order.orderitem_set.all()
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        items = cookieData['items']
        
    context={
        "items":items,
        'order': order,
    }
    return render(request, 'carts/checkout.html',context)    


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, order_completed=False)

    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    
    if action == 'add':
        orderItem.quantity = orderItem.quantity+1
    elif action == 'remove':
        orderItem.quantity = orderItem.quantity - 1
    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    request.session['cart'] = order.get_items
    return JsonResponse({'cart_items': order.get_items})
   



def processOrder(request):  

    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer=customer, order_completed=False)
        total = float(data['userForm']['total'])
        order.transaction_id = transaction_id
    
        if total == float(order.get_cart_total):
                order.order_completed = True
                request.session['cart'] = 0 
        order.save()

        if order.shipping == True:
            Shipping.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['zipcode']
            )
            

    else:
        print('User is not logged in') 
    return JsonResponse('Payment complete!',safe=False)

