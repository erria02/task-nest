from django.urls import path
from .views import CreateAutoParkApiView, CreateCarApiView, ListAutoParkApiView
urlpatterns = [
    path('create/auto_park', CreateAutoParkApiView.as_view()),
    path('create/car/<int:pk>', CreateCarApiView.as_view()),
    path('list/auto_park',ListAutoParkApiView.as_view()),
]