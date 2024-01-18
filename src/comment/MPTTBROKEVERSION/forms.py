"""
Forms for the comment app.
"""
from django import forms
from comment.models import Comment
from mptt.forms import TreeNodeChoiceField

from captcha.fields import CaptchaField


class CommentForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['text', 'file', 'captcha']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mother_comment'] = TreeNodeChoiceField(
            queryset=Comment.objects.all(),
            required=False,
            widget=forms.HiddenInput()
        )