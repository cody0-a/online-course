
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course_list.urls')),
    path('api/', include('course_list.urls')),

]
