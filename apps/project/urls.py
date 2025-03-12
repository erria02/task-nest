from django.urls import path
from .views import ListProjectApiView


urlpatterns = [
    path('list/', ListProjectApiView.as_view(),),
]