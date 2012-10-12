"""
Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
Released under the BSD 3-Clause license
http://opensource.org/licenses/BSD-3-Clause
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('sight.views',
    url(r'^$', 'index'),
    url(r'^register/$', 'register'),
    url(r'^signin/$', 'signin'),
    url(r'^signin/(?P<account>\w+)/$', 'signin_account'),
    url(r'^user/(?P<user>\w+)/$', 'user'),
    url(r'^user/(?P<user>\w+)/picture/$', 'picture'),
    url(r'^user/(?P<user>\w+)/upload/$', 'upload'),
    url(r'^user/(?P<user>\w+)/(?P<pic>\w+)/$', 'modify'),
)
