from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def letshop(request):
    return render(request, 'shop/letshop.html')
