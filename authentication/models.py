from django.db import models
from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    Gender_Type = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('Other', 'Other'),
    ]

    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=Gender_Type)
    occupation = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
