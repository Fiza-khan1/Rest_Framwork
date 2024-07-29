from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField
import uuid

class CustomUser(AbstractUser):
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    history = HistoricalRecords()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def save(self, *args, **kwargs):
        self.username = f"{self.first_name}-{self.last_name}"
        super(CustomUser, self).save(*args, **kwargs)

    

    


