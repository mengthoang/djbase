'''
Created on May 17, 2020

@author: User
'''
from rest_framework import serializers
from rest_framework.fields import empty
from allauth.account.forms import SignupForm
from collections import OrderedDict

from . import UserSerializer

class SignupSerializer(serializers.Serializer):
    username  = serializers.CharField()
    email     = serializers.EmailField()
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    
    def __init__(self, instance=None, data=empty, **kwargs):
        serializers.Serializer.__init__(
                self, instance=instance, data=data, **kwargs
            )
        self.new_user = None
        self.signup_form = None
    
    def validate(self, attrs):
        self.signup_form = SignupForm(attrs)
        if False == self.signup_form.is_valid():
            errors = OrderedDict()
            form_errors = dict(self.signup_form.errors)
            for error_field in form_errors.keys():
                errors[error_field] = form_errors[error_field]
            
            raise serializers.ValidationError(errors)
        
        return serializers.Serializer.validate(self, attrs)
    
    def save(self, **_kwargs):
        request = self.context.get('request')
        if self.signup_form is not None:
            self.new_user = self.signup_form.save(request)
        return self.new_user

    def to_representation(self, _instance):
        new_user = self.new_user
        if new_user is None:
            return dict()
        return UserSerializer(instance=new_user).data
