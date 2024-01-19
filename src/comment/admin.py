"""
Admin module for comment app.
"""

from django.contrib import admin
from comment.models import Comment
from mptt.admin import MPTTModelAdmin


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'text', 'parent', 'karma', 'file', 'created') # noqa
#     list_filter = ('created', 'karma')
#     search_fields = ('username', 'email', 'text')

admin.site.register(Comment, MPTTModelAdmin)
