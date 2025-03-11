from rest_framework.serializers import ModelSerializer
from .models import ProfileModel
from django.contrib.auth import get_user_model
from django.db.transaction import atomic

UserModel = get_user_model()

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'nickname', 'bio')
        
class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'password', 'profile', 'is_superuser', 'is_active', 'is_admin', 'created_at', 'updated_at')
        read_only_fields = ('is_superuser', 'is_active', 'id', 'is_admin')
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }
    
    @atomic
    def create(self, validated_data):
        profile = validated_data.pop("profile")
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create_user(profile=profile, **validated_data)
        user.save()
        return user
        
        
        
