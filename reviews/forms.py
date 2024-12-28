from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["title", "content", "rating"]
        widgets = {
            "rating": forms.Select(choices=[(i, i) for i in range(1, 6)]),
        }
