"""
Models for comment app
"""
from django.contrib.auth import get_user_model
from user.models import CustomUser

from django.db import models


class CommentManager(models.Manager):
    """Manager for comment model"""

    def get_queryset(self):
        """Returns queryset with related mother`s comment and author"""
        return super().all().select_related("mother_comment", "author")


class Comment(models.Model):
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

    mother_comment = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
        verbose_name='Mother comment',
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
        """Returns comment and author"""
        return f"ID comment: {self.pk} from {self.author}"

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

    # def get_mother_comments(self):
    #     """Func for getting mother comments (first)"""
    #     return Comment.objects.filter(mother_comment__isnull=True)
    #
    # def get_reply_comments(self):
    #     """Func for getting reply comments"""
    #     return Comment.objects.filter(mother_comment=self)
