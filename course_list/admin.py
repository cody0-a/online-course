from django.contrib import admin
from .models import *

@admin.register(Course)
class AdminCourse(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')  # Customize fields to display
    search_fields = ('title', 'category')  # Enable search functionality
    list_filter = ('category',)  # Add filters in the admin interface


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ('first_name','last_name','age','sex','email')
    search_fields = ('email','first_name','last_name')
    list_filter = ('email',)


@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    list_display = ('name','city',)
    search_fields = ('name',)



class AnswerAdmin(admin.TabularInline):
    list_display = ('choice_text', 'votes')
    
@admin.register(question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')



