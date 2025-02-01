from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_students_list, name='students-list'),
    path('<int:pk>/', views.get_student, name='student-detail'),
]
