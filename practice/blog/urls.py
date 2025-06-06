from django.urls import path
from .views import get_students_list, get_student, delete_blog

urlpatterns = [
    path('', get_students_list, name='blogs_list'),
    path('<int:pk>/', get_student, name='blog_details'),
    path('<int:pk>/delete/', delete_blog)
]