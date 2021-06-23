from django.contrib import admin
from dashboard.views import index
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from carts.views import updateItem,processOrder
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',index),
    path('',include('products.urls')),
    path('cart/',include('carts.urls')),
    path('update_item/',updateItem),
    path('process_order/',processOrder)
]


urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)