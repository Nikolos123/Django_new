from datetime import timedelta
from django.utils.timezone import now

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст', default=18)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)))

    # email = models.EmailField(max_length=254, verbose_name='email address',)


    def is_activation_key_expires(self):
        if now() <= self.activation_key_expires:
            return False
        return True


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'М'),
        (FEMALE, 'Ж')
    )

    user = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)

    tagline = models.CharField(verbose_name='тэги', max_length=128, blank=True)

    about_me = models.TextField(verbose_name='о себе',max_length=512,blank=True)

    gender = models.CharField(verbose_name='пол',choices=GENDER_CHOICES,blank=True,max_length=128)

    langs = models.CharField(verbose_name='Язык', max_length=128, blank=True)

    age_form = models.DateField(verbose_name='возраст', blank=True,default='20000101')

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.userprofile.save()
