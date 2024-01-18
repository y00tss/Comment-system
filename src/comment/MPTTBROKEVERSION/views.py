"""
Views for the comment app.
"""
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from comment.models import Comment
from user.models import CustomUser

from comment.forms import CommentForm

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.contrib import messages


class CommentListView(TemplateView):
    template_name = 'comment/comment.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_comments'] = Comment.objects.filter(mother_comment__isnull=True).order_by('-created')
        context['comment_form'] = CommentForm()

        if 'reply_to' in self.request.GET:
            reply_to_id = self.request.GET['reply_to']
            context['reply_to_comment'] = get_object_or_404(Comment, pk=reply_to_id)

        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)

        if request.user.is_authenticated:
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user

                reply_to_id = request.POST.get('mother_comment')
                if reply_to_id:
                    comment.mother_comment = Comment.objects.get(pk=reply_to_id)

                comment.save()
        else:
            return redirect('Closed access')

        return redirect('index')
