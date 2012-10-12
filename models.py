"""
Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
Released under the BSD 3-Clause license
http://opensource.org/licenses/BSD-3-Clause
"""

from django.contrib.auth.models import User
from django.db import models

#class User(models.Model):
#    user = models.CharField(max_length=64)
#    password = models.CharField(max_length=64)
#    email = models.CharField(max_length=64)
#    registered = models.DateTimeField('date registered')
#    signedin = models.DateTimeField('date signed in')
#    online = models.BooleanField(default=True)
#
#    def __unicode__(self):
#        return self.user

class Album(models.Model):
    description = models.CharField(max_length=256,
                                   blank=True,
                                   null=True)
    public = models.BooleanField(default=False)
    created = models.DateTimeField('date created')
    modified = models.DateTimeField('date modified')
    user = models.ForeignKey(User,
                             blank=True,
                             null=True,
                             on_delete=models.SET_NULL)

    def __unicode__(self):
        return unicode(self.description)

class Photo(models.Model):
    description = models.CharField(max_length=256)
    public = models.BooleanField(default=False)
    original = models.CharField(max_length=256)
    modified = models.CharField(max_length=256)
    preview = models.CharField(max_length=256)
    uploaded = models.DateTimeField('date uploaded')
    edited = models.DateTimeField('date edited')
    user = models.ForeignKey(User,
                             blank=True,
                             null=True,
                             on_delete=models.SET_NULL)
    #album = models.ForeignKey(Album,
    #                          blank=True,
    #                          null=True,
    #                          on_delete=models.SET_NULL)

    def __unicode__(self):
        return unicode(self.description)
