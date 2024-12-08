from django.shortcuts import render
from .models import LoyaltyPoints

def loyalty_points_view(request):
    """Display the user's current points."""
    loyalty_points, created = LoyaltyPoints.objects.get_or_create(user=request.user)
    context = {'loyalty_points': loyalty_points}
    return render(request, 'loyalty/loyalty_points.html', context)
