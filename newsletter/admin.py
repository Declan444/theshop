from django.contrib import admin
from .models import NewsletterSubscriber


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):

    list_display = ("email", "timestamp")
    search_fields = ("email",)
    list_filter = ("timestamp",)
