from django.shortcuts import render
from .forms import CourseForm
from .models import Course
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
# Create your views here.
def index(request):
    listOfCourses = Course.objects.all()
    return render(request,'index.html',  {'listOfCourses': listOfCourses})

def aboutus(request):
    return render(request,'aboutus.html')

def course(request, id):
    course = Course.objects.get(pk=id)
    return render(request, 'course.html', context={"course": course})

def create_course(request):

    if request.method == 'POST':
        course_form = CourseForm(request.POST, request.FILES)
        if course_form.is_valid :
            course_form.save()
            # return redirect('accounts:index')
    else:
        course_form = CourseForm()


    return render(request, "courses.html", {'course_form': course_form})

class CourseView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'name': 'chegra'})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body['coursename'])
        # content = body['content']
        return JsonResponse({'name': 'chegra'})