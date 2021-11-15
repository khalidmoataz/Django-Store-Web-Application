"""store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from django.urls import path,re_path
from django.contrib import admin
from .views import Home_page,login_page,register_page
from products.views import products_list_1,product_item,featured_item
from cart.views import cart_home

urlpatterns = [
    path('', Home_page, name='home_view'),
    path('login/', login_page, name='signin_view'),
    path('register/', register_page, name='register_url_view'),
    path('cart/', include(("cart.urls",'cart'),namespace='cart')),
    re_path('shop/', include(("products.urls",'shop'),namespace='shop')),
    path('search/', include(("search.urls",'search'), namespace='search')),
    path('c/', include(("Categories.urls",'categorys'), namespace='categorys')),
    path('admin/', admin.site.urls)
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
