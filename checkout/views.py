from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'There is nothing in your bag at the moment')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QLYljFd7OibauiF4VxJGoiWVIPvtgbEnbNfoD2OL0bg11YpLb4mWda7DpEsSzkyLGOWyle7JIQTeqpscKKZZxBI00zmmG6IQG',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)