from django.urls import path
from .views import list,detail,add_comment

urlpatterns = [
    path('', list, name="list"),
    path('<int:pk>',detail,name="detail"),
    path('products/addcomment',add_comment,name="add-comment")
]
