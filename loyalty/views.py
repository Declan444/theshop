from django.shortcuts import render, redirect
from .models import LoyaltyPoints
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def loyalty_points_view(request):
    """Display the user's current points."""
    loyalty_points = LoyaltyPoints.objects.get(user=request.user)
    context = {'loyalty_points': loyalty_points}
    return render(request, 'loyalty/loyalty_points.html', context)

@login_required
def apply_loyalty_points(request):
    if request.method == "POST":
        points_to_apply = int(request.POST.get('points', 0))
        loyalty_points = request.user.loyaltypoints  # Assuming a related field in your user model
        if points_to_apply <= loyalty_points.points:
            # Calculate value of points
            point_value = points_to_apply  # Adjust conversion rate if needed
            
            # Deduct from bag total (assume stored in session)
            bag = request.session.get('shopping_bag', {})
            bag['total'] = max(bag['total'] - point_value, 0)  # Prevent negative total
            request.session['shopping_bag'] = bag

            # Deduct points from user's loyalty balance
            loyalty_points.points -= points_to_apply
            loyalty_points.save()

            messages.success(request, "Loyalty points applied successfully!")
        else:
            messages.error(request, "You don't have enough points.")
    return redirect('shopping_bag')