from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers


USER = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ('fullname', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     if USER.objects.filter(email=validated_data['email']).exists():
    #         raise serializers.ValidationError(
    #             {
    #                 "email": "Email already exists."
    #             }
    #         )
    #     password = validated_data.pop('password')
    #     user = USER(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=128, required=True)
    user = serializers.ReadOnlyField

    def validate(self, attrs):
        attrs = super().validate(attrs)
        email = attrs['email']
        password = attrs['password']
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError(
                {
                    "message": "Invalid Credentials"
                }
            )

        else:
            self.validated_user = user
            return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER
        fields = ['id', 'fullname', 'email']
        read_only_fields = ['id']

