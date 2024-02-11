from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from store.models import *


# Create your views here.

def index(request):
    return render(request,'index.html')

def single_product(request):
    return render(request,'single.html')

def about_us(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact.html')

def signup(request):
    if request.method=="POST":
        first=request.POST.get('fname')
        second=request.POST.get('sname')
        n=' '
        username=first+n+second
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if password == password1:
            if User.objects.filter(username=username,email=email,password=password).exists():
                messages.info(request,'username already exists')
                print('already have')
            else:
                user=User.objects.create_user(username,email,password)
                user.save()
                return redirect('store:login')
        else:
            print('wrong password')
    return render(request,'signup.html')

def logine(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password1 = request.POST.get('password')
        user=authenticate(username=username,password=password1)
        if user is not None:
            login(request,user)
            return redirect('store:product_list')
        else:
            messages.info(request,'user not exist')
            print('user not  exist')
            return redirect('store:login')
    return render(request,'login.html')


def logoute(request):
    logout(request)
    return redirect('store:product_list')
def product_list(request):
    
    products_female = Product.objects.filter(catogory=Category.objects.get(id=1))
    products_male = Product.objects.filter(catogory=Category.objects.get(id=2))
    products_kids = Product.objects.filter(catogory=Category.objects.get(id=3))
    return render(request, 'index.html', {'mproducts': products_male,'fproducts':products_female,'cproducts':products_kids})

def view_cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.product.price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
	product = Product.objects.get(id=product_id)
	cart_item, created = CartItem.objects.get_or_create(product=product, 
													user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('store:view_cart')

# def remove_from_cart(request, item_id):
# 	cart_item = CartItem.objects.get(id=item_id)
# 	cart_item.delete()
# 	return redirect('store:view_cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('store:view_cart')


def forgot_password(request):
     return render(request,'forgot.html')


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'
