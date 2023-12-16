from django.shortcuts import render
from .forms import CourseForm
from .models import Course
from django.http import HttpResponse, JsonResponse
from django.views import View
import json
from django.core.paginator import Paginator
from django.forms.models import model_to_dict
# Create your views here.
def index(request):
    
    if(request.GET.get("search")):
        listOfCourses = Course.objects.filter(title__contains=request.GET['search'])
    else:
        listOfCourses = Course.objects.all()
    paginator = Paginator(listOfCourses, 8) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'index.html',  {'listOfCourses': page_obj})

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

def delete(request):
    Course.objects.all().delete()
    return JsonResponse({'name': 'chegra'})
def custom_404(request, ex):
    return render(request, "errorpage.html")
def custom_500(request):
    return render(request, "errorpage.html")
class CourseView(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'name': 'chegra'})
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        new_course = Course.objects.create(title=body['title'], link=body['link'])
        content = body['title']
        return JsonResponse({"id": new_course.id, 'name': content,  "link" : new_course.link})
    
