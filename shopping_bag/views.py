from django.shortcuts import render


# Create your views here.



def view_shopping_bag(request):
    """
    A view to display the shopping bag
    """
    
    return render(request, 'shopping_bag/shopping_bag.html')