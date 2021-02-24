'''
Created on May 17, 2020

@author: User
'''
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
            User, unique=True, on_delete=models.CASCADE
        )
    address = models.CharField(max_length=140, null=True, blank=True)
    gender = models.CharField(max_length=140, null=True, blank=True)

    # Create profile for each created user.
    @classmethod
    def handle_user_created(cls, sender, instance, created,**kwargs):
        if True == created:
            profile = cls(user=instance)
            profile.save()