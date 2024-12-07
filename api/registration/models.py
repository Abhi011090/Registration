from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class UserRegistration(AbstractBaseUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)
    mobile_no = models.BigIntegerField(unique=True)
    whatsapp_no = models.BigIntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=250)
    registration_no = models.CharField(max_length=100)
    vat_no = models.CharField(max_length=100)
    address = models.TextField()

    ROLE_CHOICES = [
        ("owner", "Owner"),
        ("director", "Director"),
        ("finance_manager", "Finance Manager"),
        ("general_manager", "General Manager"),
        ("user", "User"),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    designation = models.CharField(max_length=250)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "mobile_no"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
