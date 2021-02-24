from django.urls import path
from .views import SignupApiView
from .views import ProfileApiView
from .views import CurrentProfileApiView
from .views import ProfileListApiView

urlpatterns = [
    path('signup/', SignupApiView.as_view(), name='v1_user_signup'),
    path('profile/', CurrentProfileApiView.as_view(), name='v1_user_current_profile'),
    path('profiles/', ProfileListApiView.as_view(), name='v1_user_profile_list'),
    path('<int:id>/profile/', ProfileApiView.as_view(), name='v1_user_profile')
    
]
