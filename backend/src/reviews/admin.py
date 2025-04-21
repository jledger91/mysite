from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Admin class for the Review model."""

    list_display = (
        "user",
        "film",
        "rating",
        "date_submitted",
    )
