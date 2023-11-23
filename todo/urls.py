# todo/urls.py
from django.urls import path
from .views import TodosAPIView, TodoAPIView, CompletedTodosAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('todo/<int:pk>/', TodoAPIView.as_view()),
    path('todo/completed/', CompletedTodosAPIView.as_view()),
]
