from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, userName, email, password):
        user = self.model(email = email,userName = userName)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userName, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            userName = userName,
            password = password,
        )
        user.is_admin   = True
        user.is_active  = True  
        user.is_staff   = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email           = models.EmailField(max_length=40, unique=True, primary_key=True)
    firstName       = models.CharField(max_length=15)
    lastName        = models.CharField(max_length=15)
    userName        = models.CharField(max_length=15)

    date_joined     = models.DateTimeField(default=timezone.now)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['userName']

    object = MyAccountManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin 
    def has_module_perms(self, add_label):
        return True
    def __str__(self):
        return self.email
