from loyalty.models import LoyaltyPoints


def loyalty_points_processor(request):
    """
    Add loyalty points to the context for logged-in users.
    """
    if request.user.is_authenticated:
        try:
            loyalty_points = LoyaltyPoints.objects.get(user=request.user)
            return {'loyalty_points': loyalty_points.points}
        except LoyaltyPoints.DoesNotExist:
            return {'loyalty_points': 0}
    return {'loyalty_points': None}