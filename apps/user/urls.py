from django.urls import path
from apps.auth.urls import urlpatterns
from .views import GetMe, CreateUserApiView, ListUserApiView

urlpatterns = [
    path('me/', GetMe.as_view(), name='get_me'),
    path('create/', CreateUserApiView.as_view(), name='create_user'),
    path('list/', ListUserApiView.as_view(), name='list_users')
]