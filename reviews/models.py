from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    """
    A model to store reviews about the site
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    rating = models.PositiveIntegerField()  # Rating between 1 and 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.username} - {self.title}"