"""
URL configuration for src project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import (
    path,
    include,
)

from user import views as user_views

from comment import views as comment_views

from comment.service.karma import vote_karma

urlpatterns = [
    path("admin/", admin.site.urls),

    # main pages
    path('captcha/', include('captcha.urls')),
    # path("", comment_views.CommentListView.as_view(), name="index"),
    path("", comment_views.CommentListView, name="index"),
    path(
        'vote_karma/<int:comment_id>/<str:action>/',
        vote_karma,
        name='vote_karma',
    ),
    path(
        'reply_comment/<int:comment_id>/',
        comment_views.reply_comment,
        name='reply',
    ),


    # user pages
    path('login/', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path("user/", user_views.profileview, name="user"),
    path("user/singup/", user_views.signup, name="signup"),
    path("user/edit/", user_views.edit_profile, name="edit_profile"),

    # additional pages
    path("stop/", user_views.closed_access, name="Closed access"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
