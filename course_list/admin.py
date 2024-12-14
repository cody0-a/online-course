from django.contrib import admin
from .models import Course

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')  # Customize fields to display
    search_fields = ('title', 'category')  # Enable search functionality
    list_filter = ('category',)  # Add filters in the admin interface
