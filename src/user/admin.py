"""
Admin module for user app.
"""

from django.contrib import admin
from user.models import CustomUser

admin.site.register(CustomUser)
