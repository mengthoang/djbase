'''
Created on May 17, 2020

@author: User
'''
from rest_framework import serializers
from avatar.forms import UploadAvatarForm
from collections import OrderedDict
from rest_framework.fields import empty
from avatar.models import Avatar
from avatar.signals import avatar_updated

from user.models import Profile
from djbase.utils import FileUtil

from . import UserSerializer

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source='user.id', read_only=True)
    first_name = serializers.CharField(
            source='user.first_name',
            required=False,
            read_only=True
        )
    last_name = serializers.CharField(
            source='user.last_name',
            required=False,
            read_only=True
        )
    email = serializers.EmailField(
            source='user.email',
            required=False,
            read_only=True
        )
    avatar = serializers.SerializerMethodField()
    
    class Meta:
        model  = Profile
        fields = '__all__'

    def __init__(self, instance=None, data=empty, **kwargs):
        initial_data = dict()
        if empty != data:
            initial_data = data
            self.user_serializer = self._init_user_serializer(
                    instance, initial_data
                )
        
        serializers.ModelSerializer.__init__(self, instance=instance, data=data, **kwargs)
    
    def _init_user_serializer(self, instance, initial_data):
        email = initial_data.get('email', instance.user.email)
        first_name = initial_data.get('first_name', instance.user.first_name)
        last_name = initial_data.get('last_name', instance.user.last_name)
        user_serializer = None
        if instance:
            user_data = dict(
                    id=instance.user.id, email=email,
                    first_name=first_name, last_name=last_name
                )
            user_serializer = UserSerializer(
                    data=user_data, instance=instance.user
                )
        return user_serializer

    def get_avatar(self, instance):
        avatar = instance.user.avatar_set.filter(primary=True).first()
        if avatar is None:
            return None
        return avatar.get_absolute_url()

    def validate_avatar(self):
        user = self.context.get('user')
        avatar = self.initial_data.get('avatar')
        if avatar is None or 'base64' not in avatar or user is None:
            return None
        avatar = FileUtil.get_file_from_data_url(avatar)[0]
        avatar_form = UploadAvatarForm(None, dict(avatar=avatar), user=user)
        
        if False == avatar_form.is_valid():
            errors = OrderedDict()
            form_errors = dict(self.signup_form.errors)
            for error_field in form_errors.keys():
                errors[error_field] = form_errors[error_field]
            raise serializers.ValidationError(errors)
        
        return avatar
    
    def validate_user(self):
        if not self.user_serializer:
            return None
        
        if False == self.user_serializer.is_valid():
            errors = OrderedDict()
            form_errors = dict(self.user_serializer.errors)
            for error_field in form_errors.keys():
                errors[error_field] = form_errors[error_field]
            raise serializers.ValidationError(errors)
        return self.user_serializer

    def validate(self, attrs):
        self.avatar = self.validate_avatar()
        self.validate_user()
        validated_data = serializers.ModelSerializer.validate(self, attrs)
        return validated_data
    
    def save_avatar(self, instance):
        keys = self.initial_data.keys()
        if 'avatar' in keys and \
            (self.avatar is not None or self.initial_data.get('avatar') is None):
            avatar = instance.user.avatar_set.filter(primary=True).first()
            if avatar is not None:
                avatar.primary = False
                avatar.save()
                return avatar_updated.send(
                        sender=Avatar, user=instance.user, avatar=avatar
                    )
        elif self.avatar is None:
            return None
        
        if self.avatar:
            avatar = Avatar(user=instance.user, primary=True)
            image_file = self.avatar
            avatar.avatar.save(image_file.name, image_file)
            avatar.save()
            avatar_updated.send(sender=Avatar, user=instance.user, avatar=avatar)
            return avatar
    
    def update(self, instance, validated_data):
        if self.user_serializer:
            self.user_serializer.save()
        return serializers.ModelSerializer.update(self, instance, validated_data)
    
    def save(self, **kwargs):
        profile = serializers.ModelSerializer.save(self, **kwargs)
        self.save_avatar(profile)
        return profile
