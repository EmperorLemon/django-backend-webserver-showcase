from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Accounts(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = "Account"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"