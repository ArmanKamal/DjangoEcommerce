import json
from products.models import Product


def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}
        
    items = []
    order = {'get_cart_total':0, 'get_items':0,'shipping':False}
    request.session['cart_items'] = order['get_items']
    for i in cart:
        try:
            request.session['cart_items'] += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            order['get_cart_total'] += total
            order['get_items'] += cart[i]['quantity']

            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price':product.price,
                    'image': product.image
                },
                'quantity': cart[i]['quantity'],
                'get_total': total
            }
            items.append(item)
            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'order':order, 'items':items}
    
