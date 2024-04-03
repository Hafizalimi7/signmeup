from django.contrib.auth import get_user_model
from django.test import TestCase


User = get_user_model()

class UserModelTestCase(TestCase):
  def test_create_user(self):
    user = User.objects.create(
      first_name ="Test1",
      last_name="Last1",
      email="test@gmail.com",
      username="Test123",
      password="Test123"
    )
    self.assertEqual(user.first_name, "Test1")
    self.assertEqual(user.last_name, "Last1")
    self.assertEqual(user.email, "test@gmail.com")
    self.assertTrue(user.is_active)
    self.assertFalse(user.is_admin)
    