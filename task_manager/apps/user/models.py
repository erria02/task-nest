from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import  UserManager
# Create your models here.

class ProfileModel(models.Model):
    class Meta:
        db_table = 'profiles'
    
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=25, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
class UserModel(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'auth_users'
    
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    profile = models.OneToOneField(ProfileModel, on_delete=models.CASCADE, related_name='user')
    is_superuser = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    objects = UserManager()
    
    
    
    
    
