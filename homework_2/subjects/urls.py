from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_courses_list, name='subjects-list'),
    path('<int:pk>/', views.get_course, name='subject-detail'),
]
