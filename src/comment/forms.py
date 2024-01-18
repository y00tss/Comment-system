"""
Forms for the comment app.
"""
from django import forms
from comment.models import Comment

from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    """Form to create a comment and pass the captcha."""
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['text', 'file', 'captcha']
