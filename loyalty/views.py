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
    context = {"loyalty_points": loyalty_points}
    return render(request, "loyalty/loyalty_points.html", context)


@login_required
def apply_loyalty_points(request):
    if request.method == "POST":
        shopping_bag = request.session.get("shopping_bag", {})
        grand_total = sum(
            item["quantity"] * item["price"] for item in shopping_bag.values()
        )

    if request.method == "POST":
        points_to_apply = request.POST.get("points", None)
        if not points_to_apply or not points_to_apply.isdigit():
            messages.error(request, "Invalid points value.")
            return redirect("shopping_bag:view_shopping_bag")
        points_to_apply = int(points_to_apply)
        try:
            loyalty_points = LoyaltyPoints.objects.get(user=request.user)
        except LoyaltyPoints.DoesNotExist:
            messages.error(request, "You don't have any loyalty points.")
            return redirect("shopping_bag:view_shopping_bag")

        # Assuming grand total is stored in session or can be retrieved
        grand_total = request.session.get("grand_total", 0)
        if grand_total <= 1:
            points_needed = 0
        else:
            # Calculate points needed to bring grand total to zero
            points_needed = min(points_to_apply, grand_total - 1)
        if points_needed > loyalty_points.points:
            messages.error(request, "You don't have enough loyalty points.")
            return redirect("shopping_bag:view_shopping_bag")

        # Update grand total and loyalty points
        loyalty_points.points -= points_needed
        loyalty_points.save()
        request.session["points_applied"] = points_needed
        grand_total_after_points = grand_total - points_needed
        request.session["grand_total"] = max(grand_total_after_points, 0)
        messages.success(
        request,
        f"{points_needed} loyalty points applied successfully!",
        extra_tags="loyalty_success",
)
        return redirect("checkout")
    messages.error(request, "Invalid request method.")
    print("Invalid request method used.")  # Debug
    return redirect("shopping_bag:view_shopping_bag")
