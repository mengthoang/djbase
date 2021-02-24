'''
Created on May 17, 2020

@author: User
'''

from django.contrib import admin
from user.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address', 'gender')
    search_fields = ('id', 'user__username','user__email')

admin.site.register(Profile, ProfileAdmin)
