from django.urls import path
from todo import views
urlpatterns = [
    path('', views.index, name='todolist'),
    path('updateTodo/<str:pk>/', views.updateTodo, name='updateTodo'),
    path('deleteTodo/<str:pk>/', views.deleteTodo, name='deleteTodo'),
    path('todo/<str:pk>/', views.getTodo, name='getTodo'),
]
