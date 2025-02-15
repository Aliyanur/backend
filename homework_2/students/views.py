from django.shortcuts import render, get_object_or_404
from .models import Student

def get_students_list(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def get_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, 'student-details.html', {'student': student})

