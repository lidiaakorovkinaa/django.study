from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'show_on_site']
    list_editable = ['show_on_site']