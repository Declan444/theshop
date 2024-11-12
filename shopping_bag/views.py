from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Products
from django.http import JsonResponse 
from products.models import Products


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
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity', 1)) 
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')  
    bag = request.session.get('bag', {})

    if size:
        # Add item with specific size to bag
        if item_id in bag:
            if size in bag[item_id].get('items_by_size', {}):
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]['items_by_size'][size]}')
            else:
                # Create entry for new size
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')
        else:
            # Create entry for item with size
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')
    else:
        # Add item without size to bag
        if item_id in bag:
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your shopping bag')

    # Save updated bag in session
    request.session['bag'] = bag

    print(request.session['bag'])  # Debugging: Remove in production
    return redirect(redirect_url)

def adjust_shopping_bag(request, item_id):
    """
    Adjust the quantity of the product in the shopping bag
    """
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity', 1)) 
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]['items_by_size'][size]}')
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your shopping bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
             bag.pop(item_id)
             messages.success(request, f'Removed {product.name} from the shopping bag.')

    request.session['bag'] = bag
    return redirect(reverse("view_shopping_bag"))

def remove_from_shopping_bag(request, item_id):
    product = get_object_or_404(Products, pk=item_id)
    try:
        # Retrieve the shopping bag from the session
        bag = request.session.get('bag', {})


        # Use str(item_id) to match the string keys in session data
        if str(item_id) in bag:
            del bag[str(item_id)]  # Remove the item using string key
            request.session['bag'] = bag  # Update session with modified bag
            messages.success(request, f'Removed {product.name} from your shopping bag.')
            # Return success response
            return JsonResponse({'status': 'success'}, status=200)
            
        else:
            # Return error response if item_id is not found
            return JsonResponse({'error': 'Item not found in the bag'}, status=400)

    except Exception as e:
        # Return error response with exception details
        return JsonResponse({'error': str(e)}, status=500)
    
    