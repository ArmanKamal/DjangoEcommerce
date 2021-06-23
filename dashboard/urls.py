from django.urls import path
from .views import create,index

urlpatterns = [
    path('',index,name="dashboard"),
    path('products/create', create, name="product-create"),
 
]
