"""
Admin module for comment app.
"""

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from comment.models import Comment

#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('author', 'text', 'parent', 'karma', 'file', 'created')
#     list_filter = ('created', 'karma')
#     search_fields = ('username', 'email', 'body')


admin.site.register(Comment)
