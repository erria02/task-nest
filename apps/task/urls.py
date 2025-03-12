from django.urls import path
from apps.task.views import CreateTaskApi, ListTaskApi


urlpatterns = [
    path('list/', ListTaskApi.as_view() ),
    path('create/', CreateTaskApi.as_view())
]
