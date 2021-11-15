from django.shortcuts import render
from products.models import Product

def products_search_list_1(request):
    search_element = request.GET.get('q',None)
    filter_items   = request.GET
    if search_element is not None:
        p_query =  Product.objects.filter_items(filter_items).search(search_element)
        context = {
        "all_products": p_query,
        "search_element":search_element,
        }
    return render(request, "search/all_products.html", context)
