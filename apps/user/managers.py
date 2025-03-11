from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, password, *args, **kwargs):
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_admin', True)
        user = self.create_user(email, password, profile_id=1, **kwargs)
        return user