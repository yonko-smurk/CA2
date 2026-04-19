from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=250, null = False, blank = False)
    last_name = models.CharField(max_length=250, null = False, blank = False)
    email = models.CharField(max_length=250, null = False, blank = False)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, default='')

    


    