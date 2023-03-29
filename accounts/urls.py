from django.urls import path,include
from accounts.views import *
from rest_framework import routers
from knox.views import LogoutView


router = routers.DefaultRouter()
router.register(r'user-register', RegisterView, basename='task')
urlpatterns = [ 
    path('',include(router.urls)),
    path('get-login-otp-mobile/',ValidatePhoneSendOTP.as_view(),name='get-login-otp-mobile'),
    path('verify-login-otp-mobile/',VerifyPhoneOTPView.as_view(),name='login-otp-verify'),
    path('logout/', LogoutView.as_view(), name='knox_logout')
]


