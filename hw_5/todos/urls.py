from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('<int:id>/', views.todo_detail, name='todo_detail'),
    path('<int:id>/delete', views.todo_delete, name='todo_delete'),
    path('<int:id>/edit/', views.todo_update, name='todo_update'),
]
