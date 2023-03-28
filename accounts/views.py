from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from accounts.serializers import RegisterSerializer
from accounts.utils import otp_generator
from knox.models import AuthToken
from django.contrib.auth import login
from rest_framework import permissions, generics, status
import requests


User = get_user_model()

# Create your views here.


class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'response': serializer.data,
            'scucess': True,
            'message': 'User created successfully',
            'status': status.HTTP_201_CREATED,

        })


def send_otp(phone):
    """
    This is an helper function to send otp to session stored phones or 
    passed phone number as argument.
    """

    if phone:

        key = otp_generator()
        phone = str(phone)
        otp_key = str(key)

        link = f'https://2factor.in/API/R1/?module=TRANS_SMS&apikey=7c59cf94-d129-11ec-9c12-0200cd936042&to={phone}&from=MMBook&templatename=mymedbook&var1={otp_key}&var2={otp_key}'

        result = requests.get(link, verify=False)

        return otp_key
    else:
        return False


class ValidatePhoneSendOTP(APIView):
    def post(self, request, *agrs, **kwargs):
        try:
            phone_number = request.data.get('phone')

            if phone_number:
                phone = str(phone_number)
                user = User.objects.filter(phone__iexact=phone)

                if user.exists():
                    data = user.first()
                    old_otp = data.otp
                    new_otp = send_otp(phone)
                    if old_otp:
                        data.otp = new_otp
                        data.save()
                        return Response({
                            'otp': new_otp,
                            'message': 'OTP sent successfully',
                            'status': status.HTTP_200_OK,
                        })
                    else:
                        data.otp = new_otp
                        data.save()
                        return Response({
                            'otp': new_otp,
                            'message': 'OTP sent successfully',
                            'status': status.HTTP_200_OK,
                        })

                else:
                    return Response({
                        'message': 'User not found ! please register',
                        'status': status.HTTP_404_NOT_FOUND,
                    }
                    )
            else:
                return Response({
                    'message': 'Phone number is required',
                    'status': status.HTTP_400_BAD_REQUEST,
                })
        except Exception as e:
            return Response({
                'message': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
            })


# verify otp
class VerifyPhoneOTPView(APIView):
    def post(self, request, format=None):
        try:
            phone = request.data.get('phone')
            otp = request.data.get('otp')

            if phone and otp:
                user = User.objects.filter(phone__iexact=phone)
                if user.exists():
                    user = user.first()
                    if user.otp == otp:
                        login(request, user)
                        return Response({
                            'status': True,
                            'details': 'Login Successfully',
                            'token': AuthToken.objects.create(user)[1],
                            'response': {
                                'id': user.id,
                                'name': user.fname + ' ' + user.lname,
                                'email': user.email,
                                'phone': user.phone,
                                'address': user.address,
                                'city': user.city,
                            }})
                    else:
                        return Response({'message': 'OTP does not match'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'message': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Phone or OTP is missing'}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            return Response({
                'status': False,
                'message': str(e),
                'details': 'Login Failed'
            })


# logout api view
class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        try:
            request.user.auth_token.delete()
            return Response({
                'message': 'Logout successfully',
                'status': status.HTTP_200_OK,
            })
        except Exception as e:
            return Response({
                'message': str(e),
                'status': status.HTTP_400_BAD_REQUEST,
            })
