from django.shortcuts import render
from products.models import Products

# Create your views here.


def index(request):
    """
    A view to display the weekly bargain product on the index page
    """
    weekly_bargain = Products.objects.filter(is_weekly_bargain=True).first()

    context = {
        "weekly_bargain": weekly_bargain,
    }

    return render(request, "shop/index.html", context)
