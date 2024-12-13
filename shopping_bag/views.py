from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from products.models import Products
from loyalty.models import LoyaltyPoints

def view_shopping_bag(request):
    """
    A view to display the shopping bag
    """

    bag = request.session.get('bag', {})
    loyalty_points = None

    if request.user.is_authenticated:
        try:
            from loyalty.models import LoyaltyPoints
            loyalty_points = LoyaltyPoints.objects.get(user=request.user)
        except LoyaltyPoints.DoesNotExist:
            loyalty_points = LoyaltyPoints.objects.create(user=request.user, points=0)

    context = {
        'bag': bag,
        'loyalty_points': loyalty_points,
    }
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
        if str(item_id) in bag:
            if size in bag[str(item_id)].get('items_by_size', {}):
                bag[str(item_id)]['items_by_size'][size] += quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[str(item_id)]["items_by_size"][size]}')
            else:
                bag[str(item_id)]['items_by_size'][size] = quantity
                messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')
        else:
            bag[str(item_id)] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added size {size.upper()} {product.name} to your shopping bag')
    else:
        if str(item_id) in bag:
            bag[str(item_id)] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[str(item_id)]}')
        else:
            bag[str(item_id)] = quantity
            messages.success(request, f'Added {product.name} to your shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_shopping_bag(request, item_id):
    """
    Adjust the quantity of the product in the shopping bag
    """
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    size = request.POST.get('product_size', None)
    bag = request.session.get('bag', {})

    if size:
        if str(item_id) in bag and 'items_by_size' in bag[str(item_id)]:
            if quantity > 0:
                bag[str(item_id)]['items_by_size'][size] = quantity
                messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[str(item_id)]["items_by_size"][size]}')
            else:
                del bag[str(item_id)]['items_by_size'][size]
                if not bag[str(item_id)]['items_by_size']:
                    bag.pop(str(item_id))
                messages.success(request, f'Removed size {size.upper()} {product.name} from your shopping bag')
        else:
            messages.error(request, 'Item or size not found in bag.')
    else:
        if quantity > 0:
            bag[str(item_id)] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[str(item_id)]}')
        else:
            bag.pop(str(item_id))
            messages.success(request, f'Removed {product.name} from the shopping bag.')

    request.session['bag'] = bag
    return redirect(reverse("view_shopping"))


def remove_from_shopping_bag(request, item_id):
    product = get_object_or_404(Products, pk=item_id)
    try:
        bag = request.session.get('bag', {})
        if str(item_id) in bag:
            del bag[str(item_id)]
            request.session['bag'] = bag
            messages.success(request, f'Removed {product.name} from your shopping bag.')
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'error': 'Item not found in the bag'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
