from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self,email, first_name, last_name,password=None,phone=None):
        if not email:
            raise ValueError("Email is strogly required!")
        if not first_name:
            raise ValueError("First name is required!")
        if not last_name:
            raise ValueError("Last name is required!")    

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,email, first_name, last_name,password,phone=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_admin     = True
        user.is_staff     = True
        user_is_superuser = True
        user.save(using=self._db)
        return user

class ShopUser(AbstractBaseUser):
    email               = models.EmailField(verbose_name="email",unique=True)
    first_name          = models.CharField(verbose_name="first name",max_length=300,null=True)
    last_name           = models.CharField(verbose_name="last name",max_length=300,null=True)
    phone               = models.CharField(max_length=60,null=True,blank=True)
    is_admin            = models.BooleanField(default=False)
    is_staff            = models.BooleanField(default=False)
    is_superuser        = models.BooleanField(default=False)
    registration_date   = models.DateTimeField(verbose_name='registered at',auto_now_add=True,null=True)
    last_login          = models.DateTimeField(verbose_name='last login',auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name',]

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin
    def has_module_perms(self,app_label):
        return True
