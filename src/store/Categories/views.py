from django.shortcuts import render
from .models import AllCategory,MainCategory,SubCategory1,SubCategory2
from django.db.models import Q
from products.models import Product
from cart.models import cart
def Electronics_page(request):
    return render(request,"Electronics/home.html",{})

def category_page(request,cat_slug=None):
    all_cats = MainCategory.objects.all()
    Sub_cat_1 = SubCategory1.objects.all()
    the_cart = cart.objects.new_or_create_cart(request)
    cat_object           = AllCategory.objects.get(slug=cat_slug)
    lookup  = Q(SubCategory1__name=cat_object.name) | Q(SubCategory2__name=cat_object) | Q(MainCategory__name=cat_object)
    products_cat         = Product.objects.filter(lookup)
    context = {
    'products_cat':products_cat,
    'cat_object':cat_object,
    'the_cart':the_cart,
    'all_cats':all_cats,
    'Sub_cat_1':Sub_cat_1
    }
    return render(request,"categories/category.html",context)
