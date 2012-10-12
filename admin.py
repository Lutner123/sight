"""
Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
Released under the BSD 3-Clause license
http://opensource.org/licenses/BSD-3-Clause
"""

from django.contrib import admin
from sight.models import Album, Photo
from django.contrib.auth.models import User

class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1

class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
                'fields': ['id', 'username']}),
        ('Information', {
                'fields': ['email', 'password', 'last_login', 'date_joined'],
                'classes': ['collapse']}),
    ]
    inlines = [AlbumInline, PhotoInline]
    list_display = ('username', 'email')

# Error: The model User is already registered
#admin.site.register(User, UserAdmin)
