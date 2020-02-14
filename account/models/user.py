from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, nickname, email, password, birthdate, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=nickname, nickname=nickname, email=email, birthdate=birthdate **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nickname, email, password, birthdate, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(nickname, email, password, birthdate, **extra_fields)


class User(AbstractUser):
    nickname = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthdate = models.DateField(default="2000-01-01")

    # admin
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'birthdate']
    objects = UserManager()

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def str(self):
        return self.email