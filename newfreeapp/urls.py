from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('create-course/', views.create_course),
    path('course/<int:id>/', views.course, name="course"),
    path('delete/api/', views.delete),
    path('CourseView/api/', views.CourseView.as_view()),
]