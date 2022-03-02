from django.urls import path

from .views import UserCreateAPIView, LoginAPIView, UserProfileRetrieveUpdateAPIView

app_name = 'user'
urlpatterns = [
    path('register', UserCreateAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('current-user', UserProfileRetrieveUpdateAPIView.as_view(),
        name='current-user'),
]
