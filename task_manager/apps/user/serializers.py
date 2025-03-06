from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .models import ProfileModel

UserModel=get_user_model()

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = '__all__'
        
class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'profile', 'is_superuser', 'is_staff'
        )
        read_only_fields=(
            'is_superuser',
            'is_staff'
        )
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }
    
    @atomic
    def create(self, validated_data):
        profile = validated_data.pop('profile')
        profile = ProfileModel.objects.create(**profile)
        user = UserModel.objects.create(profile=profile, **validated_data)
        user.save()
        return user
