from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('register/', views.register_view, name='register_page'),
    path('logout/', views.logout_view, name='logout_page'),

    path('', views.todo_list_view, name='todo_list_page'),
    path('todos/<int:pk>/', views.todo_detail_view, name='todo_detail_page'),
    path('todos/<int:pk>/delete/', views.delete_todo_view, name='delete_todo_page'),
    path('todos/<int:pk>/edit/', views.edit_todo_view, name='edit_todo_page'),
]
