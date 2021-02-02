from django.contrib import admin

from mysite.models import Film


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'release_date',
        'duration',
        'rating',
    )
