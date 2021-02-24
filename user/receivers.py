'''
Created on May 17, 2020

@author: User
'''
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from user.models import Profile
# 
class SignalReceiver(object):
     
    @classmethod
    def connect(cls):
        post_save.connect(
                Profile.handle_user_created,
                sender=User,
                dispatch_uid="Profile.handle_user_created"
            )
