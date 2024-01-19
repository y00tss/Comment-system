"""
Views for the comment app.
"""
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
)
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage,
)

from comment.models import Comment

from comment.forms import CommentForm, ReplyForm

from comment.service.comment_settings import MAX_NODE_LEVEL


def CommentListView(request):
    """View for comments list and comment form"""

    allcomments = Comment.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page) # noqa
    except PageNotAnInteger:
        comments = paginator.page(1) # noqa
    except EmptyPage:
        comments = paginator.page(paginator.num_pages) # noqa

    user_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.save()
        else:
            return redirect('Closed access')
    else:
        comment_form = CommentForm()
    return render(
        request,
        'comment/comment.html',
        {
            'comments': user_comment,
            'comment_form': comment_form,
            'allcomments': allcomments,
            'MAX_NODE_LEVEL': MAX_NODE_LEVEL,
        })


def reply_comment(request, comment_id):
    """View for reply comment form"""
    parent = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment_form = ReplyForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.parent = parent  # Set the parent comment
                comment.save()
                return redirect('index')
        else:
            return redirect('Closed access')
    else:
        comment_form = ReplyForm()

    return render(
        request,
        'comment/comment.html',
        {'comment_form': comment_form},
    )
