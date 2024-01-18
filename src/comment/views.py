"""
Views for the comment app.
"""
from django.views.generic import TemplateView
from django.shortcuts import redirect

from comment.models import Comment

from comment.forms import CommentForm


class CommentListView(TemplateView):
    """View for comment list"""
    template_name = 'comment/comment.html'
    paginate_by = 25

    # queryset = Comment.objects.all().filter(mother_comment_id__isnull=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            mother_comment__isnull=True
        ).order_by('-created')
        # context['mother_comments'] = Comment.objects.filter(mother_comment__isnull=False).order_by('-created') # noqa
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.save()
        else:
            return redirect('Closed access')
        return redirect('index')
