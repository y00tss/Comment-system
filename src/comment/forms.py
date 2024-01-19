"""
Forms for the comment app.
"""
from django import forms

from comment.models import Comment

from captcha.fields import CaptchaField


# from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    """Form to create a comment and pass the captcha."""
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['parent'].widget.attrs.update(
        #     {'class': 'd-none'})
        # self.fields['parent'].label = ''
        # self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('text', 'file', 'captcha')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(CommentForm, self).save(*args, **kwargs)


class ReplyForm(forms.ModelForm):
    """Form to create a reply comment."""
    captcha = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['parent'].widget.attrs.update(
        #     {'class': 'd-none'})
        # self.fields['parent'].label = ''
        # self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ('text', 'file', 'captcha')

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def save(self, *args, **kwargs):
        Comment.objects.rebuild()
        return super(ReplyForm, self).save(*args, **kwargs)
