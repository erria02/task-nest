from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from core.models import BaseModel
from apps.user.managers import UserManager

# Create your models here.

class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profiles'
    
    nickname = models.CharField(max_length=20)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

class UserModel(AbstractBaseUser, PermissionsMixin, BaseModel):
    class Meta:
        db_table = 'auth_users'
        
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    profile = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='user')
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    objects = UserManager()
