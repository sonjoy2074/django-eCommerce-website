from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# To automatically create a profile when a user is created, we will use the post_save signal.
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    """A custom manager to deal with emails as unique identifiers for auth"""
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, null=False)
    is_active = models.BooleanField(_('Active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    is_staff = models.BooleanField(_('Staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'))

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=264, blank=True)
    address_1 = models.TextField(max_length=300, blank=True)
    city = models.CharField(max_length=264, blank=True)
    zipcode = models.CharField(max_length=10, blank=True)
    country = models.CharField(max_length=264, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}'s profile"

    def is_fully_filled(self):
        fields_name = [f.name for f in self._meta.get_fields()]
        for field_name in fields_name:
            value = getattr(self, field_name)
            if value is None or value == '':
                return False
        return True

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
