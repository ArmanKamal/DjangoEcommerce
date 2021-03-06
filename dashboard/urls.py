from django.urls import path
from .views import create,index,delete,order_view,edit,update_product,order_details_view

urlpatterns = [
    path('',index,name="dashboard"),
    path('products/create', create, name="product-create"),
    path('products/edit/<int:id>', edit, name="product-edit"),
    path('products/edit/<int:id>/update', update_product, name="update_product"),
    path('products/delete/<int:id>',delete,name="product-delete"),
    path('orders',order_view,name="product-order"),
    path('order/<int:id>',order_details_view,name="order_details_view")
 
]
