from django.urls import path
from .views import course_list_create, course_detail,index, python_courses

urlpatterns = [
    path('',index, name = 'base'),
    path('python/', python_courses, name='python-courses'),
    path('css/', python_courses, name='css-courses'),
    path('html/', python_courses, name='html-courses'),
    path('javascript/', python_courses, name='javascript-courses'),
    path('django/', python_courses, name='django-courses'),
    path('flask/', python_courses, name='flask-courses'),
    path('react/', python_courses, name='react-courses'),
    path('quest_and_ans/', python_courses, name='questions-and-answers'),
    path('courses/', course_list_create, name='course-list-create'),
    path('courses/<int:pk>/', course_detail, name='course-detail'),
]