from django.shortcuts import render, redirect


# Create your views here.



def view_shopping_bag(request):
    """
    A view to display the shopping bag
    """
    
    return render(request, 'shopping_bag/shopping_bag.html')

def add_to_shopping_bag(request, item_id):

    """
    Add a product quantity to the shopping bag
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)

