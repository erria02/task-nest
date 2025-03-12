from django.urls import path
from apps.tag.views import ListTagApiView

urlpatterns = [
    path('list/', ListTagApiView.as_view())
]