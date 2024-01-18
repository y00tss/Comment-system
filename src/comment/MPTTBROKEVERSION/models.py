"""
Models for comment app
"""
from django.contrib.auth import get_user_model
from user.models import CustomUser

from mptt.models import MPTTModel, TreeForeignKey

from django.db import models


class _CommentManager(models.Manager):
    """Manager for comment model"""

    def all(self):
        """Returns queryset with related mother`s comment and author"""
        return super().all().select_related("mother_comment", "author")


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

    mother_comment = TreeForeignKey(
        'self', on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        verbose_name='Mother comment',
    )

    is_reply = models.BooleanField(
        default=False,
        verbose_name='Is Reply'
    )

    voters = models.ManyToManyField(
        get_user_model(),
        related_name='voted_comments',
        blank=True,
    )

    karma = models.IntegerField(
        default=0
    )

    file = models.FileField(
        upload_to="comment_files/",
        blank=True,
        null=True,
        verbose_name="Attached comment file",
    )

    objects = _CommentManager()

    def __str__(self) -> str:
        """Returns comment ID and author"""
        return f"ID comment: {self.pk} from {self.author}"

    def get_mother_comments(self):
        """To see all comments related to the mother comment"""
        return Comment.objects.filter(mother_comment=self)

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

    class Meta:
        ordering = ['-created']
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
