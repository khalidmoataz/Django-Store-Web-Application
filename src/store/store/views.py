from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import myform,loginForm,SignUpForm
from django.contrib.auth import authenticate,login,get_user_model
from Categories.models import MainCategory,SubCategory1
from products.models import Product
from cart.models import cart
def Home_page(request):
    the_cart = cart.objects.new_or_create_cart(request)
    all_cats = MainCategory.objects.all()
    Sub_cat_1 = SubCategory1.objects.all()
    Electronics_category = MainCategory.objects.get(name="Electronics")
    Fashion_category     = MainCategory.objects.get(name="Fashion")
    all_Electronics_products = Product.objects.filter(MainCategory=Electronics_category).order_by('-id')[:6]
    all_Fashion_category_products = Product.objects.filter(MainCategory=Fashion_category).order_by('-id')[:6]
    context = {
    'the_cart':the_cart,
    'all_cats' :all_cats,
    'Sub_cat_1':Sub_cat_1,
    'all_Electronics_products':all_Electronics_products,
    'all_Fashion_category_products':all_Fashion_category_products,
    'Electronics_category':Electronics_category,
    'Fashion_category':Fashion_category,
    }
    return render(request,"Home.html",context)

def login_page(request):
    form = loginForm(request.POST or None)
    login_info = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        loginuser = authenticate(request, username=username, password=password)
        if loginuser is not None:
            login(request, loginuser)
            return redirect("/shop") # Got to home page
        else:
            return redirect("/login") # Got to Login Again
    return render(request,"auth/login.html",login_info)

User = get_user_model()
def register_page(request):
    form = SignUpForm(request.POST or None)
    signup_info = {
        "form" : form
    }
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        the_user = User.objects.create_user(username, email, password)
        print(the_user)
    return render(request,"auth/register.html", signup_info)
