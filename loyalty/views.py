from django.shortcuts import render, redirect
from .models import LoyaltyPoints
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def loyalty_points_view(request):
    """Display the user's current points."""
    try:
        loyalty_points = LoyaltyPoints.objects.get(user=request.user)
    except LoyaltyPoints.DoesNotExist:
        loyalty_points = None  
    context = {'loyalty_points': loyalty_points}
    return render(request, 'loyalty/loyalty_points.html', context)

@login_required
def apply_loyalty_points(request):
    if request.method == "POST":
        points_to_apply = request.POST.get('points', None)
        
        if not points_to_apply or not points_to_apply.isdigit():
            messages.error(request, "Invalid points value.")
            return redirect('shopping_bag:view_shopping_bag')

        points_to_apply = int(points_to_apply)

        try:
            loyalty_points = LoyaltyPoints.objects.get(user=request.user)
        except LoyaltyPoints.DoesNotExist:
            messages.error(request, "You don't have any loyalty points.")
            return redirect('shopping_bag:view_shopping_bag')

        if points_to_apply > loyalty_points.points:
            messages.error(request, "You don't have enough loyalty points.")
            return redirect('shopping_bag:view_shopping_bag')

        
        request.session['points_applied'] = points_to_apply

        
        loyalty_points.points -= points_to_apply
        loyalty_points.save()

        messages.success(request, f"{points_to_apply} loyalty points applied successfully!")
        return redirect('checkout')
    
    messages.error(request, "Invalid request method.")
    return redirect('checkout')
