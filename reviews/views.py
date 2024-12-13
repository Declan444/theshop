from django.shortcuts import render, redirect, get_object_or_404
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
            return redirect('reviews')  
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

@login_required
def delete_review(request, review_id):
    """Allows a user to delete their own review."""
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted successfully.')
        return redirect('reviews')  

    template = 'reviews/delete_review.html'
    context = {'review': review}
    return render(request, template, context)

@login_required
def edit_review(request, review_id):
    """Allows a user to edit their own review."""
    review = get_object_or_404(Review, id=review_id, user=request.user)  

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated successfully.')
            return redirect('reviews')  
    else:
        form = ReviewForm(instance=review)

    template = 'reviews/edit_review.html'
    context = {'form': form, 'review': review}
    return render(request, template, context)
