from django.shortcuts import render
import requests
from django.templatetags.static import static

def index(request):
    context = {'title': 'Index'}
    return render(request, 'index.html',context)

def shop(request):
    url = static('data/product.json')
    full_url = f"http://localhost:8000/{url}"

    response = requests.get(full_url)
    data = response.json()

    context = {'title': 'Shop','data':data }

    return render(request, 'shop.html',context)

def productdetails(request):
    context = {'title': 'ProductDetails'}

    return render(request, 'productdetail.html', context)

def contact(request):
    context = {'title': 'Contact'}
    return render(request,'contact.html',context)

def about(request):
    context = {'title': 'About'}
    return render(request,'aboutus.html',context)

def checkout(request):
    context = {'title': 'Checkout'}
    return render(request,'checkout.html',context)

def cart(request):
    context = {'title': 'Cart'}
    return render(request,'cart.html',context)













