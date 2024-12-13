from django.contrib import admin
from .models import LoyaltyPoints

@admin.register(LoyaltyPoints)
class LoyaltyPointsAdmin(admin.ModelAdmin):
    list_display = ('user', 'points')
