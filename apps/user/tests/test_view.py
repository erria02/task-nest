from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from apps.user.models import ProfileModel

UserModel = get_user_model()

class UserViewsTest(APITestCase):

    def setUp(self):
        self.admin_user = UserModel.objects.create_superuser(
            email="admin@gmail.com",
            password="adminpass"
        )
        self.regular_user = UserModel.objects.create_user(
            email="user@gmail.com",
            password="userpass"
        )
        self.profile = ProfileModel.objects.create(
            nickname="Tester",
            bio="Test bio"
        )
        self.regular_user.profile = self.profile
        self.regular_user.save()

        self.user_token = self.client.post(reverse("token_obtain_pair"), {"email": "user@gmail.com", "password": "userpass"}).data.get("access")
        self.admin_token = self.client.post(reverse("token_obtain_pair"), {"email": "admin@gmail.com", "password": "adminpass"}).data.get("access")

    def test_get_me_authenticated(self):
        """Тестуємо отримання даних поточного користувача"""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        response = self.client.get(reverse("get_me"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "user@gmail.com")

    def test_get_me_unauthenticated(self):
        """Тестуємо отримання поточного користувача без авторизації"""
        response = self.client.get(reverse("get_me"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_users_as_admin(self):
        """Тестуємо отримання списку користувачів адміністратором"""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_token}")
        response = self.client.get(reverse("list_users"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)  # Мінімум 2 користувача (admin + user)

    def test_list_users_as_non_admin(self):
        """Тестуємо отримання списку користувачів звичайним користувачем"""
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.user_token}")
        response = self.client.get(reverse("list_users"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_user(self):
        """Тестуємо створення нового користувача"""
        data = {
            "email": "newuser@gmail.com",
            "password": "newuserpass",
            "profile": {
                "nickname": "NewUser",
                "bio": "New user bio"
            }
        }
        response = self.client.post(reverse("create_user"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(UserModel.objects.filter(email="newuser@gmail.com").exists())

    def test_create_user_invalid_data(self):
        """Тестуємо створення користувача з некоректними даними"""
        data = {
            "email": "",
            "password": "short",
            "profile": {
                "nickname": "NoEmail",
                "bio": "No email test"
            }
        }
        response = self.client.post(reverse("create_user"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("email", response.data)
