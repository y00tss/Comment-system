"""
User models.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom user model."""

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Undefined', 'Undefined'),
    ]

    username = models.CharField(
        max_length=128,
        unique=True,
        blank=True,
        null=False,
        verbose_name='Username',
    )

    password = models.CharField(
        max_length=128,
        blank=True,
        verbose_name='Password',
    )

    sex = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default='Undefined',
        verbose_name='Gender'
    )

    avatar = models.CharField(
        'Images',
        max_length=255,
        default='https://i.ibb.co/pxsZbty/thin-line-suspect-person-icon-600nw-2154459203.webp',  # noqa
        blank=True,
    )

    class Meta:
        """Meta"""
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username

    def save(self, *args, **kwargs):
        # Your save logic here
        super().save(*args, **kwargs)


"""
Override related_name for groups and user_permissions
"""
CustomUser._meta.get_field(
    'groups').remote_field.related_name = 'custom_user_groups'
CustomUser._meta.get_field(
    'user_permissions').remote_field.related_name = 'custom_user_permissions'
