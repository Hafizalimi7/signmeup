from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):
  def create_user(self, first_name, last_name, username, email, password, date_of_birth, is_admin=False, is_active=True):
    user = self.model(
      first_name, 
      last_name, 
      username,
      email = self.normalize_email(email),
      date_of_birth=date_of_birth
    )
    user.is_admin=False
    user.is_active=True
    user.set_password(password)
    user.save(using=self._db)
  
  def create_superuser(self, email, password):
    user = self.create_user(
      email=email,
      password=password
    )
    user.is_admin=True
    user.is_active=True
    user.save(using=self._db)