"""
URL configuration for src project.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views

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
    path("home/", comment_views.CommentListView.as_view(), name="index"),
    path(
        'vote_karma/<int:comment_id>/<str:action>/',
        vote_karma,
        name='vote_karma'
    ),

    # user pages
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("user/", user_views.profileview, name="user"),
    path("user/singup/", user_views.signup, name="signup"),
    path("user/edit/", user_views.edit_profile, name="edit_profile"),

    # additional pages
    path("stop/", user_views.closed_access, name="Closed access"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
