from django.urls import path
from .views import CreateTaskView, ListTaskView, CreateTagView, ListTagView, UpdateTaskView, TagUpdateView

urlpatterns = [
    path('create',CreateTaskView.as_view()),
    path('list', ListTaskView.as_view()),
    path('update/<int:pk>', UpdateTaskView.as_view()),
    path('tag/create', CreateTagView.as_view()),
    path('tag/list', ListTagView.as_view()),
    path('tag/update/<int:pk>', TagUpdateView.as_view())
] 