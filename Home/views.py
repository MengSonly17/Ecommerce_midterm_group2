from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    return render(request, 'base.html')

def index(request):
    return HttpResponse('Hello World!',status=200)