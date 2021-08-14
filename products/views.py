from re import sub
from django.core.checks.messages import Error
from django.shortcuts import redirect, render
from ecommerce.utils import cookieCart
from .models import Product
from ratings.models import Comment
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
    comments = Comment.objects.filter(product=product)
    context = {
            "product": product,
            "comments":comments
        }
    return render(request, "products/detail.html",context)

def add_comment(request):
    if request.user.is_authenticated:
        if request.POST:
            subject = request.POST['subject']
            comment = request.POST['comment']
            product_id = request.POST['product_id']
            product = Product.objects.get(id=product_id)

            Comment.objects.create(user = request.user, subject=subject, comment=comment,product=product)
            return redirect(f'/{product_id}')
    else:
        return redirect('/login')
    