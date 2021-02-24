'''
Created on May 17, 2020

@author: User
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializers import SignupSerializer

class SignupApiView(APIView):
    
    def post(self, request):
        post_data = request.data
        serializer = self.get_serializer(data=post_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
    
    def get_serializer_context(self):
        return dict(
                request=self.request
            )
    
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return SignupSerializer(*args, **kwargs)
