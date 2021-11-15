from django.urls import path,re_path
from .views import products_search_list_1
from products.views import product_item

urlpatterns = [
    path('', products_search_list_1,name='query'),
    re_path('(?P<pk>[-@\w]+)/', product_item),
]
