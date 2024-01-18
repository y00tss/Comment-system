"""
User views
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect

from user.forms import SignUpForm, ProfileEditForm


# from general.views import BaseView

@login_required
def profileview(request):
    """Views for Profile pages for authenticated users."""
    user = request.user
    return render(
        request,
        'user/user.html',
        {'user': user}
    )


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(
            request.POST,
            request.FILES,
            instance=request.user
        )
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)
            user.save()
            return redirect('user')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(
        request,
        'user/edit_profile.html',
        {'form': form, 'title': 'Edit profile'}
    )


def signup(request):
    """Sign up page for new users."""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user')
    else:
        form = SignUpForm()
    return render(
        request,
        'user/signup.html',
        {'form': form, 'title': 'Registration'}
    )


def closed_access(request):
    """Closed access page for unauthenticated users."""
    return render(
        request,
        'user/closed.html',
        {'title': 'Closed Access'}
    )
