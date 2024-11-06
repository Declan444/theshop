from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Products  # Adjust import if needed


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
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity not provided
    redirect_url = request.POST.get('redirect_url')
    size = request.POST.get('product_size')  # Retrieves size if present, otherwise None
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