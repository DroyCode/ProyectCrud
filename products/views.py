from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from .models import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def myproducts(request):
    products = Product.objects.all()
    return render(request, 'myproducts.html', {'products': products})


def add_to_cart(request):
    products = Product(request.POST or None)
    if products:
        products.save()
        return redirect('myproducts')
    #return render(request, 'add_to_cart.html')


def new(request):
    return HttpResponse('New Products')




