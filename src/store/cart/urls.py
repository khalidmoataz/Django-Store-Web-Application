from django.urls import path,re_path
from .views import cart_home,cart_update

urlpatterns = [
    path('', cart_home, name='home'),
    path('update/', cart_update, name='update'),
]
