# django modules
from django.db.models import (
    CharField,
    EmailField,
    BooleanField,
    DateField,
    IntegerField,
    DateTimeField,
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = EmailField(unique=True)
    fullname = CharField(max_length=150, unique=True)
    username = CharField(max_length=150, blank=True, null=True)
    first_name = CharField(max_length=150, blank=True, null=True)
    last_name = CharField(max_length=150, blank=True, null=True)
    phone = CharField(max_length=150, blank=True, null=True)
    city = CharField(max_length=150, blank=True, null=True)
    department = CharField(max_length=150, blank=True, null=True)
    country = CharField(max_length=150, blank=True, null=True)

    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("manager", "Manager"),
        ("employee", "Employee"),
    ]
    role = CharField(max_length=20, choices=ROLE_CHOICES, default="employee")
    birth_date = DateField(null=True, blank=True)
    salary = IntegerField(null=True, blank=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    date_joined = DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]

    def __str__(self):
        return self.email
