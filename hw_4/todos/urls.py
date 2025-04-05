from django.urls import path
from .views import get_students_list, get_student, delete_todo, edit_todo, get_todo_lists_list, get_todo_list_todos, edit_todo_list, delete_todo_list

urlpatterns = [
    path('', get_students_list, name='todos_list'),
    path('todo_lists/', get_todo_lists_list, name='todo_lists_list_page'),
    path('todo_lists/<int:pk>/todos', get_todo_list_todos, name ='todo_list_todo_list'),
    path('todo_lists/<int:pk>/edit', edit_todo_list, name ='edit_todo_lists'),
    path('todo_lists/<int:pk>/delete', delete_todo_list, name ='delete_todo_lists'),


    path('<int:pk>/', get_student, name='todo_details'),
    path('todos/<int:pk>/edit/', edit_todo, name='edit_todo'),
    path('<int:pk>/delete/', delete_todo)
]

#todo - product
#todo_list - category