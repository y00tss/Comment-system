"""
Models for comment app
"""
from django.contrib.auth import get_user_model
from django.db import models

from user.models import CustomUser

from mptt.models import MPTTModel, TreeForeignKey


class Comment(MPTTModel):
    """Model for comment"""
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Author',
    )

    text = models.TextField(
        max_length=1000,
        blank=False,
        null=False,
        verbose_name='Comment text'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creation',
    )

    level = models.PositiveIntegerField(
        default=0,
    )

    lft = models.PositiveIntegerField(
        default=0
    )

    rght = models.PositiveIntegerField(
        default=0,
    )

    tree_id = models.PositiveIntegerField(
        default=0,
    )

    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
    )

    voters = models.ManyToManyField(
        get_user_model(),
        related_name='voted_comments',
        blank=True,
    )

    karma = models.IntegerField(
        default=0
    )

    file = models.ImageField(
        upload_to="comment_files/",
        blank=True,
        null=True,
        verbose_name="Attached comment file",
    )

    def __str__(self) -> str:
        """Returns comment and author with truncated text"""
        truncated_text = self.text[:50] if len(self.text) > 50 else self.text
        return f"Author: {self.author} - Text: {truncated_text}"

    def karma_up(self, user):
        """Increase karma by 1 per user, once"""
        if user.is_authenticated and user not in self.voters.all():
            self.karma += 1
            self.voters.add(user)
            self.save()

    def karma_down(self, user):
        """Decrease karma by 1 per user, once"""
        if user.is_authenticated and user not in self.voters.all():
            self.karma -= 1
            self.voters.add(user)
            self.save()

    class MPTTMeta:
        """Meta class for MPTT"""
        order_insertion_by = ['-created']
