from django.contrib.auth.backends import UserModel
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """Test to check a new user creation with email"""
        email = 'test@gmail.com'
        password = 'Test@1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(Self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDON.COM'
        user = get_user_model().objects.create_user(
            email, 'test123'
        )

        Self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test uf a valid email was passed by the user"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Create a super user test"""
        user = get_user_model().objects.create_superuser(
            'test@london.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
