from django.db.models import (
    CharField,
    EmailField,
    BooleanField,
    DateField,
    DecimalField,
    DateTimeField,
)
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, fullname, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, fullname, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        return self.create_user(email, fullname, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = EmailField(unique=True)
    fullname = CharField(max_length=150)
    username = CharField(max_length=150, unique=True)
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
    salary = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    date_joined = DateTimeField(default=timezone.now)
    last_login = DateTimeField(null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["fullname"]
    objects = CustomUserManager()

    def __str__(self):
        return self.email