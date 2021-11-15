from django.urls import path,re_path
from products.views import products_list_1,product_item,featured_item

urlpatterns = [
    path('', products_list_1,name='query'),
    path('', products_list_1,name='query1'),
    re_path('(?P<pk>[-@\w]+)/', product_item),
]
