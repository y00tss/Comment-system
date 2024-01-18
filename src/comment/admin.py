"""
Admin module for comment app.
"""

from django.contrib import admin
from comment.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'mother_comment', 'karma', 'file', 'created') # noqa
    list_filter = ('created', 'karma')
    search_fields = ('username', 'email', 'text')
