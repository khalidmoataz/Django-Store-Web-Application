from django.shortcuts import render
from django.http import Http404
from .models import Product
from cart.models import cart

def products_list_1(request):
    the_cart = cart.objects.new_or_create_cart(request)
    filter_items = request.GET
    q = Product.objects.filter_items(filter_items)
    elements = q.count()
    context = {
    "all_products": q,
    "size": elements,
    "the_cart":the_cart
    }
    return render(request, "products/products.html", context)

def product_item(request, pk=None, *args, **kwargs):
    try:
        item_query = Product.objects.get(slug=pk)
    except Product.DoesNotExist:
        raise Http404("Not Exist")
    except:
        print('error')
    context = {
    "item": item_query
    }
    return render(request, "products/item.html", context)

def featured_item(request):
    item_query = Product.objects.get_featured()
    context = {
    "item" : item_query
    }
    return render(request, "products/featured.html", context)
