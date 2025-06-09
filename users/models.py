from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.managers import SoftDeletableManager
from model_utils.models import UUIDModel, SoftDeletableModel

class UserManager(BaseUserManager, SoftDeletableManager):
    pass

# Create your models here.
class User(UUIDModel, AbstractUser, SoftDeletableModel):
    user_id = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    first_name = None
    last_name = None
    REQUIRED_FIELDS = []
    email = None
    EMAIL_FIELD = None

    objects = UserManager()
