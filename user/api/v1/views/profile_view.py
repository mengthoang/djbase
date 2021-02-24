'''
Created on May 17, 2020

@author: User
'''
from rest_framework.generics import UpdateAPIView, RetrieveAPIView, ListAPIView
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from rest_framework import status
from django.contrib.auth.models import User

from user.models import Profile
from ..serializers.profile_serializer import ProfileSerializer
from ..permissions.profile_permission import IsAdminUserOrProfileOwner
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class CurrentProfileApiView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUserOrProfileOwner]
    
    def get(self, _request):
        profile = self.get_object()
        serializer = self.get_serializer(instance=profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_object(self):
        try:
            profile = self.queryset.get(user=self.request.user)
            return profile
        except ObjectDoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            exception = APIException()
            exception.status_code = status_code
            raise exception

class ProfileApiView(RetrieveAPIView, UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUserOrProfileOwner]
    
    def get_object(self):
        try:
            user_id = self.kwargs.get('id')
            profile = self.queryset.get(user=user_id)
            self.check_object_permissions(self.request, profile)
            return profile
        except ObjectDoesNotExist:
            status_code = status.HTTP_404_NOT_FOUND
            exception = APIException()
            exception.status_code = status_code
            raise exception
    
    def get_serializer_context(self):
        context = RetrieveAPIView.get_serializer_context(self)
        user_id = self.kwargs.get('id')
        user    = User.objects.filter(id=user_id).first()
        context.update(dict(user=user))
        return context

class ProfileListApiView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]


