from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class userProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField()
    birthdy = models.DateField()
    mobile = models.CharField()
    gender = models.CharField()
    email = models.CharField()