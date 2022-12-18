from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager
from common.models import BaseModel
# Create your models here.

class User(AbstractBaseUser, BaseModel):
    username = models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects : UserManager = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = []

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"username : {self.username}"