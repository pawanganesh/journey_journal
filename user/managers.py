from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, fullname, email, password, **extra_fields):
        if not fullname:
            raise ValueError(_('Full name must be set'))
        if not email:
            raise ValueError(_('Email must be set'))
        user = self.model(fullname=fullname, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,  fullname, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        extra_fields['is_active'] = True

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(fullname, email, password, **extra_fields)
