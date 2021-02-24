'''
Created on May 17, 2020

@author: User
'''
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField(required=False, allow_blank=True)
    last_name = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    date_joined = serializers.DateTimeField(read_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'date_joined')
