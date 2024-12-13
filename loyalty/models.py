from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class LoyaltyPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.points} points"

    def add_points(self, amount_spent):
        """Adds points based on the amount spent."""
        try:
            points_earned = int(amount_spent)
            if points_earned < 0:
                raise ValueError("Amount spent cannot be negative")
        except (ValueError, TypeError):
            raise ValueError("Invalid amount spent value")

        self.points += points_earned
        self.save()

    def redeem_points(self, points_to_redeem):
        """Reduces points after redemption, ensuring the user has enough."""
        if points_to_redeem < 0:
            raise ValueError("Points to redeem cannot be negative")
        if self.points >= points_to_redeem:
            self.points -= points_to_redeem
            self.save()
            return True
        else:
            raise ValueError("Insufficient points to redeem")

# Create/update LoyaltyPoints when a new User is created
@receiver(post_save, sender=User)
def create_or_update_user_loyalty_points(sender, instance, created, **kwargs):
    if created:
        LoyaltyPoints.objects.create(user=instance)
    elif not hasattr(instance, 'loyaltypoints'):
        LoyaltyPoints.objects.create(user=instance)
    else:
        instance.loyaltypoints.save()

