from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from carts.views import updateItem,processOrder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',include('dashboard.urls')),
    path('',include('products.urls')),
    path('cart/',include('carts.urls')),
    path('update_item/',updateItem),
    path('process_order/',processOrder)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

