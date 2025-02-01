from django.shortcuts import render, get_object_or_404
from .models import Course

def get_courses_list(request):
    courses = Course.objects.all()
    return render(request, 'index2.html', {'courses': courses})

def get_course(request, pk):
    course = get_object_or_404(Course, id=pk)
    return render(request, 'subject-details.html', {'course': course})
