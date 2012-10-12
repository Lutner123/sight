"""
Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
Released under the BSD 3-Clause license
http://opensource.org/licenses/BSD-3-Clause
"""

from django.contrib.auth import models, authenticate, login
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from sight.models import Photo, Album

def index(request):
    context = {}
    return render_to_response('sight/index.html', context)

def signin(request):
    context = {}

    if 'account' in request.POST:
        account = request.POST['account'].lower()
        password = request.POST['password']

        user = authenticate(username = account, password=password)
        if user:
            if user.is_active:
                login(request, user)
            else:
                context['error_acc_inactive'] = True
        else:
            context['error_acc_inval'] = True

        if context == {}:
            return HttpResponseRedirect(reverse('sight.views.user',
                                                args=[account]))

        context['account'] = account
    return render_to_response('sight/signin.html', context,
                              context_instance=RequestContext(request))

def signin_account(request, account):
    return render_to_response('sight/signin.html',
                              { 'account' : account },
                              context_instance=RequestContext(request))

def register(request):
    import re
    from django.core.validators import email_re

    context = {}
    if 'account' in request.POST:
        account = request.POST['account'].lower()
        email = request.POST['email'].lower()
        password = request.POST['password']

        # alphanumeric and underscore symbols allowed, no more than 30
        if not re.match(r'^[a-zA-Z0-9_]{1,30}$', account):
            context['error_acc_inval'] = True

        if not email_re.match(email):
            context['error_email'] = True

        if request.POST['password2'] != password:
            context['error_password'] = True

        if context == {}:
            try:
                user = models.User.objects.create_user(account, email, password)
                user.save()
                # Always return an HttpResponseRedirect after successfully
                # dealing with POST data. This prevents data from being posted
                # twice if a user hits the Back button.
                return HttpResponseRedirect(reverse('sight.views.signin_account',
                                                    args=[account]))
            except IntegrityError: # There is a record of the same user
                context['error_acc_registered'] = True

        context['account'] = account
        context['email'] = email
    return render_to_response('sight/register.html', context,
                              context_instance=RequestContext(request))

def user(request, user):
    context = { 'user' : user,
                'authorized': request.user.is_authenticated() }
    p = get_object_or_404(models.User, username=user)

    pictures = Photo.objects.all()
    if pictures == []:
        pictures = False
    context['pictures'] = pictures
    return render_to_response('sight/user.html', context)

def picture(request, user):
    context = { 'user' : user,
                'authorized': request.user.is_authenticated() }
    if 'account' in request.POST:
        account = request.POST['account'].lower()
    p = get_object_or_404(models.User, username=user)
    return render_to_response('sight/picture.html', context)

def upload(request, user):
    import tempfile
    import shutil
    import datetime

    FILE_UPLOAD_DIR = '/opt/webwm/sight/upload'

    def handle_uploaded_file(source):
        fd, filepath = tempfile.mkstemp(prefix = source.name + '_',
                                        dir = FILE_UPLOAD_DIR)
        with open(filepath, 'wb') as dest:
            shutil.copyfileobj(source, dest)
        return filepath

    context = { 'user' : user,
                'authorized': request.user.is_authenticated() }

    from sight.forms import DocumentForm

    form = None
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            f = request.FILES['docfile']
            filepath = handle_uploaded_file(f)

            # HACK
            filepath = filepath[17:]

            u = get_object_or_404(models.User, username=user)
            now = datetime.datetime.now()
            photo = Photo.objects.create(description = "photo",
                                         original = filepath,
                                         modified = "",
                                         preview = "",
                                         uploaded = now,
                                         edited = now,
                                         user = u)
            #photo.save(force_insert=True)
            photo.save()
            return HttpResponseRedirect(reverse('sight.views.user',
                                                args=[user]))

    form = DocumentForm()
    context['form'] = form
    return render_to_response('sight/picture.html',
                              context,
                              context_instance=RequestContext(request))

def modify(request, user, pic):
    context = { 'user' : user,
                'authorized': request.user.is_authenticated() }
    p = get_object_or_404(models.User, username=user)
    q = get_object_or_404(Photo, id=pic)

    context['pic'] = q
    return render_to_response('sight/modify.html', context)
