from datetime import timedelta
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):

    avatar = models.ImageField(upload_to='users_avatar', blank=True)

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))
    email = models.EmailField(max_length=254, verbose_name='email address',)


    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires:
            return False
        return True
