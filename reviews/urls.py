from django.urls import path
from . import views

urlpatterns = [
    path("submit_review/", views.submit_review, name="submit_review"),
    path("", views.reviews, name="reviews"),
    path("delete/<int:review_id>/", views.delete_review, name="delete_review"),
    path(
        "edit-review/<int:review_id>/", views.edit_review, name="edit_review"
    ),
]
