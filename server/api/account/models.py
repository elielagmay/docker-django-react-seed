from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not isinstance(username, basestring):
            raise ValueError('Users must have a valid username')

        if not isinstance(email, basestring):
            raise ValueError('Users must have a valid email address')

        user = self.model(
            username=username.strip().lower(),
            email=email.strip().lower(),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username, email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __unicode__(self):
        return self.username

    def clean(self):
        self.email = getattr(self, 'email', '').strip().lower()
        self.username = getattr(self, 'username', '').strip().lower()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
