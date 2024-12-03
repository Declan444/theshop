from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm

@login_required
def submit_review(request):
    """Allows a logged-in user to submit a review."""
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('reviews')  # Redirect to the reviews page
    else:
        form = ReviewForm()
    
    template = 'reviews/submit_review.html'
    context = {'form': form}
    return render(request, template, context)

def reviews(request):
    """Displays all user reviews."""
    reviews = Review.objects.all().order_by('-created_at')
    template = 'reviews/reviews.html'
    context = {'reviews': reviews}
    return render(request, template, context)
