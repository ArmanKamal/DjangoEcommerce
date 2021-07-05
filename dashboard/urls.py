from django.urls import path
from .views import create,index,delete,order_view

urlpatterns = [
    path('',index,name="dashboard"),
    path('products/create', create, name="product-create"),
    path('products/delete/<int:id>',delete,name="product-delete"),
    path('orders',order_view,name="product-order")
 
]
