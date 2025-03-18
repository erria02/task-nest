from django.urls import path
from apps.auth.urls import urlpatterns
from .views import GetMe, CreateUserApiView

urlpatterns = [
    path('/me', GetMe.as_view(), name='get_me'),
    path('create/', CreateUserApiView.as_view(), name='create_user')
]