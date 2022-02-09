import email
from email import message
from itertools import product
from django.shortcuts import redirect, render
from app.models import UserCreateForm
from django.contrib.auth import authenticate, login
from cart.cart import Cart
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def master(request):
    return render(request, "app/master.html")


def Index(request):
    category = Category.objects.all()

    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub = categoryID).order_by('-id')
    else:
        product = Product.objects.all()

    context = {
        'category': category,
        'product': product,
    }

    return render(request, "app/index.html", context)


# Creating user signup and signin functions
def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect ('index') 

    else:
        form = UserCreateForm()

    context = {
        'form':form,
    }
    return render(request,"app/signup.html", context)



# Add to cart
@login_required(login_url="/accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login/")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')




# Contact page functions
def Contact_us(request):
    if request.method == "POST":
        contact = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),

        )

        contact.save()

    return render(request, 'app/contact.html')



# Checkout
def Checkout(request):
    return render(request, 'app/checkout.html')