
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=200, unique=True, null=False)
    image = models.ImageField(upload_to="users/images/", blank=True)
    
    
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone"]
    
    def __str__(self):
        return self.first_name if self.first_name else self.username