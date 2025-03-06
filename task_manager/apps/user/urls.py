from django.urls import path
from .views import  UserCreateApi, UpdateProfileUserApi

urlpatterns = [
    path('create/', UserCreateApi.as_view()),
    path('profile/update/', UpdateProfileUserApi.as_view())
]