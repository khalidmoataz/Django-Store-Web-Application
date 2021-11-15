from django.shortcuts import render,redirect
from .models import cart
from products.models import Product
from Categories.models import MainCategory,SubCategory1
def cart_home(request):
    all_cats = MainCategory.objects.all()
    Sub_cat_1 = SubCategory1.objects.all()
    cart_object = cart.objects.new_or_create_cart(request)
    cart_products_order = cart_object.Products.order_by('-id') # Must be ordered by time added to cart
    context = {
    "my_cart" :cart_object,
    "p":cart_products_order,
    'all_cats':all_cats,
    'Sub_cat_1':Sub_cat_1
    }
    return render(request,"carts/home.html",context)

def cart_update(request):
    product_id     = request.POST.get('product_id')
    product_object = Product.objects.get(id=product_id)
    cart_object    = cart.objects.new_or_create_cart(request)
    if product_object in cart_object.Products.all():
        cart_object.Products.remove(product_id) # Add new product to cart
    else:
        cart_object.Products.add(product_id) # Add new product to cart
    return redirect("cart:home")
