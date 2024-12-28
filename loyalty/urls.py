from django.urls import path
from . import views


urlpatterns = [
    path("loyalty-points/", views.loyalty_points_view, name="loyalty_points"),
    path("apply/", views.apply_loyalty_points, name="apply_loyalty_points"),
]
