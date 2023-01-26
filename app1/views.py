from django.shortcuts import render, redirect
from django.db.models import Q
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index_view(request):
    products = Product.objects.all()

    context = {
        'products' : products
    }
    return render(request, 'app1/index.html', context)

def search_view(request):
    products = None
    product_count = 0
    if 'keyword' in request.GET:
        print(1)
        keyword = request.GET["keyword"]
        if keyword:
            print(2)
            products    = Product.objects.order_by('-created_at').filter( Q(description__icontains=keyword) | Q(name__icontains=keyword))
        product_count   = products.count()


    context={
        "products"      :   products,
        "product_count" :   product_count
    }

    return render(request, 'app1/search.html', context)

def product_view(request, pk ):
    product = Product.objects.get(id=pk)
    comments = Comment.objects.filter(product=product)

    context = {
        'product' : product,
        'comments' : comments
    }
    return render(request, 'app1/product.html', context)


def login_view(request):

    user = None 

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user.is_authenticated :
            login(request, user)
            messages.success(request, f"Login Successful ! You are now logged in as {username}.")
            return redirect('/')
        else :
            messages.error(request, f"Login failed ! username and password do not match.")

    return render(request, 'app1/loginForm.html')

def register_view(request):

    user = None

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password != confirmpassword and len(password) < 8 :
            messages.error(request, "password too short  or do not match.")

        else :
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.first_name = firstname
                user.last_name = lastname
                user.save()
                messages.success(request, f"Registered successfully!")
                return redirect('/login/')
            
            except:
                messages.error(request, "email already exists try another.") 

    return render(request, 'app1/registerForm.html')

def logout_view(request):

    logout(request)
    messages.success(request, f"Log Out Successfull ! You are now logged out.")
    return index_view(request)


def comment_add_view(request, pk ):

    comment1 = None
    product = Product.objects.get(id=pk)
    user= request.user

    user_comment = Comment.objects.filter(product = product, user= user)

    if user_comment:
        messages.error(request, f"sorry ! only one comment available!")
    else:
        if request.method == 'POST':
            rating = request.POST['rating']
            comment = request.POST['comment']

            comment1= Comment.objects.create(product= product, user = user, rating = rating,comment = comment)
            comment1.save()

        messages.success(request, f"comment added successfully")
    return redirect('product_view', pk=pk)

