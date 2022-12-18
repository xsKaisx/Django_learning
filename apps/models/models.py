from django.db import models
from apps.users.models import User
from common.models import BaseModel

# Create your models here.

class UserProfile(BaseModel):
    user = models.OneToOneField(to=User, unique=True, on_delete=models.CASCADE, related_name='profile')
    fullname = models.CharField(max_length=255, null=True, blank=True, default=None)
    mobile_number = models.CharField(max_length=255, null=True, blank=True, unique=True, default=None)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True, default = None)
    skype = models.CharField(max_length=255, null=True, blank=True, unique=True, default=None)
    bio = models.TextField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.fullname