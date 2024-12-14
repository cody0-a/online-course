from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import CourseSerializer
from .forms import CourseRegisterForm,UserProfileForm
from django.shortcuts import redirect


def index(request):
    return render(request,'course/base.html')

def python_courses(request):
    courses = Course.objects.filter(category='Python')
    if courses:
        context = {'courses': courses}
        return render(request,'course/python.html',context)

    
    return render(request,'course/python.html')


def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course-list')

def update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        course.title = request.POST.get('title')
        course.description = request.POST.get('description')
        course.category = request.POST.get('category')
        course.save()
        return redirect('course-list')
    return render(request, 'course/update.html', {'course': course})

def create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        Course.objects.create(title=title, description=description, category=category)
        return redirect('course-list')
    return render(request, 'course/create.html')
@api_view(['GET', 'POST'])
def course_list_create(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def django_courses(request):
    courses = Course.objects.filter(category='Django')
    if courses:
        context = {'courses': courses}
        return render(request,'course/django.html',context)
    return render(request,'course/django.html')


def vue_courses(request):
    courses = Course.objects.filter(category='Vue')
    if courses:
        context = {'courses': courses}
        return render(request,'course/vue.html',context)
    return render(request,'course/vue.html')

def flask_courses(request):
    courses = Course.objects.filter(category='Flask')
    if courses:
        context = {'courses': courses}
        return render(request,'course/flask.html',context)
    return render(request,'course/flask.html')

def react_courses(request):
    courses = Course.objects.filter(category='React')
    if courses:
        context = {'courses': courses}
        return render(request,'course/react.html',context)
    return render(request,'course/react.html')

def javascript_courses(request):
    courses = Course.objects.filter(category='Javascript')
    if courses:
        context = {'courses': courses}
        return render(request,'course/javascript.html',context)
    return render(request,'course/javascript.html')



def html_courses(request):
    courses = Course.objects.filter(category='html')
    if courses:
        context = {'courses': courses}
        return render(request,'course/html.html',context)
    return render(request,'course/html.html')



def css_courses(request):
    courses = Course.objects.filter(category='css')
    if courses:
        context = {'courses': courses}
        return render(request,'course/css.html',context)
    return render(request,'course/css.html')

def questions_and_answers(request):

    return render(request,'course/questions_and_answers.html')
        
@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
java
    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



def register_for_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.user.is_authenticated:
        form = CourseRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(reverse("course_list:registered_student"))

        else:
            courses_forms = CourseRegisterForm(request.POST) 
            return render(request,'course/register_for_course.html', {'courses' : courses})


def user_profile(request):
    if request.user.is_authenticated:
        forms = UserProfileForm(request.POST,request.FILES)
        if forms.is_valid:
            forms.save()
            return redirect('course_list:your_profile')

        else:
             