Problems encountered

Total order quantity value not updating in the admin. Signals being sent for update and delete. Can update and delete from the admin but not updating when 
the order form is being filled in on the site. Order is being processed and success message is being displayed, order is present on the stripe transactions page. not recording the item size. Needs to be solved.

webhook now working. Need to read documentation to allow to work. Walkthrough out of date. Fixed

emails set up but not working. Assume its because of the webhook not working for the stripe payments. Fixed

If a user applies their loyalty points but does not pay and logs out, the loyalty points are lost. Need to figure this out.

if request.user.is_authenticated:
        loyalty_points_obj = LoyaltyPoints.objects.filter(user=request.user).first()
        loyalty_points = loyalty_points_obj.points if loyalty_points_obj else 0
    else:
        loyalty_points = 0


 # Debugging information before applying points
    print(f"Grand Total before Applying Points: {grand_total}")
    print(f"User Loyalty Points (Available): {loyalty_points}")
    print(f"Points Requested to Apply: {points_applied}")

    if request.user.is_authenticated and loyalty_points > 0:
        # Dynamically calculate points to apply
        points_applied = min(loyalty_points, grand_total - 1)  
        grand_total -= points_applied  # Deduct points from the grand total
        loyalty_points -= points_applied  # Deduct applied points from user's available points

    # Debugging information
    print(f"Grand Total before Applying Points: {delivery + total}")
    print(f"User Loyalty Points (Available): {loyalty_points + points_applied}")
    print(f"Points Requested to Apply: {points_applied}")
    print(f"Grand Total after Applying Points: {grand_total}")
    print(f"User Loyalty Points (Remaining): {loyalty_points}")