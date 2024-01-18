"""
Karma service for comments
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from comment.models import Comment


def vote_karma(request, comment_id, action):
    """Function for voting karma"""
    comment = get_object_or_404(Comment, pk=comment_id)

    if action == 'up':
        comment.karma_up(request.user)
    elif action == 'down':
        comment.karma_down(request.user)

    data = {'karma': comment.karma}
    return JsonResponse(data)
