from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from .forms import ProductForm

# Create your views here.


def index(request):
    context = {
        'list_of_products' : models.Product.objects.all()   
    }

    return render(request, 'comm/index.html', context=context)


def signup(request):
    if request.method == 'GET':
        return render(request, 'comm/signup.html')
    if request.method == 'POST':
        username = request.POST['username']
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        a = User.objects.create_user(
            username=username, email=email, password=password, first_name=firstName, last_name=lastName)
        a.save()
        return render(request, 'comm/signup.html')


def signin(request):
    if request.method == 'GET':
        return render(request, 'comm/signin.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                             'PLEASE ENTER VALID DETAILS')
            return render(request, 'comm/signin.html')

def handleLogout(request):
    if User.is_authenticated:
        logout(request)
        return render(request, 'comm/index.html')
    else:
        return render(request, 'comm/index.html')

def profile(request):
    if User.is_authenticated:
        list_of_posted_products_i = models.Product.objects.all()
        list_of_posted_products = []
        for i in list_of_posted_products_i:
            if i.author == request.user:
                list_of_posted_products.append(i)
            else:
                continue
        return render(request, 'comm/profile.html' ,context={
            'list_of_posted_products':list_of_posted_products
        })
    else:
        return render(request, 'comm/login.html')

def addproduct(request):
    if request.method == 'GET':
        if User.is_authenticated:
            form = ProductForm()
            return render(request, 'comm/addproduct.html', context={
                'form':form
            })
        else:
            return render(request, 'comm/login.html')
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('/')
        return render(request, 'comm/login.html')