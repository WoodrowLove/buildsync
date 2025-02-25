from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('contractor', 'Contractor'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='contractor')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username
