from django.urls import path
from .views import list,detail

urlpatterns = [
    path('', list, name="list"),
    path('<int:pk>',detail,name="detail")
]
