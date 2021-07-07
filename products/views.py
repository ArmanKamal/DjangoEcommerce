from django.core.checks.messages import Error
from django.shortcuts import render
from ecommerce.utils import cookieCart
from .models import Product
from carts.models import Order
# Create your views here.
def list(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer, order_completed=False)
    else:
        order = {'shipping',False}
        cookieData = cookieCart(request)
    products = Product.objects.all()
    context={"products":products}
    return render(request, 'products/list.html',context)



def detail(request,pk):
    product = Product.objects.get(id=pk)
    context = {
            "product": product
        }
    return render(request, "products/detail.html",context)

def add_comment(request):
    pass