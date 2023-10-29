from django.shortcuts import render
from .forms import CourseForm
from .models import Course

# Create your views here.
def index(request):
    listOfCourses = Course.objects.all()
    return render(request,'index.html',  {'listOfCourses': listOfCourses})

def create_course(request):

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid :
            course_form.save()
            # return redirect('accounts:index')
    else:
        course_form = CourseForm()


    return render(request, "courses.html", {'course_form': course_form})