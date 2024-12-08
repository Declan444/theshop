# loyalty/models.py
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
        points_earned = int(amount_spent)  # 1 point per 1 unit of currency 
        self.points += points_earned
        self.save()

    def redeem_points(self, points_to_redeem):
        """Reduces points after redemption, ensuring the user has enough."""
        if self.points >= points_to_redeem:
            self.points -= points_to_redeem
            self.save()
            return True
        return False

# Create/update LoyaltyPoints when a new User is created
@receiver(post_save, sender=User)
def create_or_update_user_loyalty_points(sender, instance, created, **kwargs):
    if created:
        LoyaltyPoints.objects.create(user=instance)
    instance.loyaltypoints.save()
