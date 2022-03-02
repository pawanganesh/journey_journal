from django.contrib.auth import  get_user_model

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import generics, permissions, status


from rest_framework_simplejwt.tokens import AccessToken

from user.serializers import LoginSerializer, UserRegistrationSerializer, UserSerializer


USER = get_user_model()


class UserCreateAPIView(generics.CreateAPIView):
    """
    ```
    {
        "username": "shopperktomah",
        "email": "pawanlalganesh@gmail.com",
        "password": "secret@123"
    }
    ```
    """
    queryset = USER.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


class LoginAPIView(APIView):
    """
    ```
    {
        "email": "pawanlalganesh@gmail.com",
        "password": "test@123"
    }
    ```
    """
    serializer_class = LoginSerializer

    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            accesstoken = AccessToken.for_user(serializer.validated_user)
            return  Response(
                {
                    "access_token": str(accesstoken)
                }
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    
    serializer_class = UserSerializer
