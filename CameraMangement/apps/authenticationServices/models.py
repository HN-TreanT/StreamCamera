from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=255,unique=True)
    password= models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_active= models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.username