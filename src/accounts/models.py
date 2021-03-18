from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    zip_code = models.CharField(blank=True, max_length=5)
