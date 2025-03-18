from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from ..models import ProfileModel
from ..serializers import UserSerializer

UserModel = get_user_model()

class UserSerializerTest(TestCase):

    def test_user_create(self):
        data = {
            "email": "test@gmail.com",
            "password": "password",
            "profile": {
                "nickname": "Test",
                "bio": "test"
            }
        }

        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        user = serializer.save()

        self.assertTrue(UserModel.objects.filter(email="test@gmail.com").exists())

        # Перевіряємо, що пароль збережений у хешованому вигляді
        self.assertTrue(user.check_password("password"))

        # Перевіряємо, що профіль створений та прив'язаний до користувача
        self.assertTrue(ProfileModel.objects.filter(nickname="Test").exists())
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
        """Перевіряємо, що некоректні дані профілю викликають помилку"""
        data = {
            "email": "test@gmail.com",
            "password": "password",
            "profile": {
                "nickname": "",  # Нікнейм не може бути порожнім
                "bio": "Test"
            }
        }

        serializer = UserSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("nickname", serializer.errors["profile"])
