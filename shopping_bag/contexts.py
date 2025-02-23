from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Products
from loyalty.models import LoyaltyPoints


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})
    points_applied = Decimal(request.session.get("points_applied", 0))

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Products, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            shopping_bag_items.append(
                {
                    "item_id": item_id,
                    "quantity": item_data,
                    "product": product,
                }
            )
        else:
            product = get_object_or_404(Products, pk=item_id)
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * product.price
                product_count += quantity
                shopping_bag_items.append(
                    {
                        "item_id": item_id,
                        "quantity": quantity,
                        "product": product,
                        "size": size,
                    }
                )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total - points_applied

    # Store grand total in session
    request.session["grand_total"] = float(
        grand_total
    )  # Store as float to ensure JSON compatibility
    request.session.modified = True  # Mark session as modified to save changes

    context = {
        "shopping_bag_items": shopping_bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_threshold": settings.FREE_DELIVERY_THRESHOLD,
        "grand_total": grand_total,
        "points_applied": points_applied,
        "loyalty_points": (
            request.user.loyaltypoints.points
            if request.user.is_authenticated
            else 0
        ),
    }

    return context
