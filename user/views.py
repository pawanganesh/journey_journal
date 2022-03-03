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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if USER.objects.filter(email=serializer.validated_data['email']).exists():
            return Response(
                {
                    "message": "Email already exists."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        password = serializer.validated_data.pop('password')
        user = USER(**serializer.validated_data)
        user.set_password(password)
        user.save()
        accesstoken = AccessToken.for_user(user)
        return  Response(
            {
                "access_token": str(accesstoken)
            }
        )



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
