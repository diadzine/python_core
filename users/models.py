from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
TYPE_USER = (('basic', _('Basic')), ('admin', _('Admin')),)


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, name=''):
        if not email:
            msg = 'Users must have an email address'
            raise ValueError(msg)

        user = self.model(
            email=CustomUserManager.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name):
        user = self.create_user(email=email, password=password, name=name)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    """ AbstractBaseUser has: password, last_login, is_active """
    email = models.EmailField(
        verbose_name='Email', max_length=255, unique=True, db_index=True)
    name = models.TextField(verbose_name='Full Name')

    signature = models.TextField(null=True, verbose_name='Signature for articles')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', ]
    objects = CustomUserManager()

    def get_full_name(self):
        return '%s' % self.email

    def get_short_name(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.get_short_name()
