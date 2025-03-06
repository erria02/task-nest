from django.contrib.auth.models import BaseUserManager 
from django.db.models import Manager




class UserManager(BaseUserManager):
    def create_user(self, email, password, *args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_staff', True)
        user = self.create_user(email=email, password=password,  profile_id=1, **kwargs)
        user.save()
        return user        
        