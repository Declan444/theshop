from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Products
from django.http import JsonResponse 


def view_shopping_bag(request):
    """
    A view to display the shopping bag
    """
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """
    Add a product quantity to the shopping bag.
    Supports items with or without sizes.
    """
    quantity = int(request.POST.get('quantity', 1)) 
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')  
    bag = request.session.get('bag', {})

    if size:
        # Add item with specific size to bag
        if item_id in bag:
            if size in bag[item_id].get('items_by_size', {}):
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # Create entry for new size
                bag[item_id]['items_by_size'][size] = quantity
        else:
            # Create entry for item with size
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # Add item without size to bag
        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # Save updated bag in session
    request.session['bag'] = bag

    # Optional: Provide user feedback if messages are used
    product = get_object_or_404(Products, pk=item_id)
    messages.success(request, f'Added {product.name} to your bag.')

    print(request.session['bag'])  # Debugging: Remove in production
    return redirect(redirect_url)

def adjust_shopping_bag(request, item_id):
    """
    Adjust the quantity of the product in the shopping bag
    """
    quantity = int(request.POST.get('quantity', 1)) 
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
             bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse("view_shopping_bag"))

def remove_from_shopping_bag(request, item_id):
    try:
        # Retrieve the shopping bag from the session
        bag = request.session.get('bag', {})

        # Debugging print statement for checking the contents of the shopping bag
        print(f"Current shopping bag: {bag}")

        if str(item_id) in bag:
            del bag[str(item_id)]  # Ensure we are using string keys for session data
            request.session['bag'] = bag  # Save the updated shopping bag to session

            # Return success response
            return JsonResponse({'status': 'success'}, status=200)
        else:
            # Return error response if item_id is not found in the bag
            return JsonResponse({'error': 'Item not found in the bag'}, status=400)

    except Exception as e:
        # Return error response with exception details
        return JsonResponse({'error': str(e)}, status=500)
