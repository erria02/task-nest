from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from apps.user.models import ProfileModel
from apps.user.serializers import UserSerializer

UserModel = get_user_model()

class UserSerializerTest(TestCase):

    def test_user_create(self):
        user = {
            "email": "test@gmail.com",
            "password": "password",
            "profile": {
                "nickname": "Test",
                "bio": "test"
            }
        }

        serializer = UserSerializer(data=user)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()

        self.assertTrue(UserModel.objects.filter(email="test@gmail.com").exists())
        self.assertEqual(user.profile.nickname, "Test")

    def test_create_invalid_user(self):
        data = {
            "password": "password",
            "profile": {
                "nickname": "Test",
                "bio": "test"
            }
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    def test_invalid_profile_data(self):
        data = {
            "email": "test@gmail.com",
            "password": "password",
            "profile": {
                "nickname": "", 
                "bio": "Test"
            }
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("nickname", serializer.errors["profile"])
        
# efoemeofmem
