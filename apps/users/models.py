#django modules
from django.db.models import Model,CharField,EmailField,BooleanField
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,PermissionsMixin


'''
first custom user with the phone and email fields
'''
class CustomUser1(AbstractUser):
    phone=CharField(max_length=11,null=False,blank=True)
    email=CharField(max_length=255,null=True,blank=True)



'''
second custom user with the email and fullname fields
'''
class CustomUser2(AbstractBaseUser,PermissionsMixin):
    email=EmailField(unique=True)
    fullname=CharField(max_length=150,unique=True)
    is_active=BooleanField(default=False)
    is_staff=BooleanField(default=False)
    is_superuser=BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['fullname']