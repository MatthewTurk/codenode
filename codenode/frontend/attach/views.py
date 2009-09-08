######################################################################### 
# Copyright (C) 2007, 2008, 2009 
# Alex Clemesha <alex@clemesha.org> & Dorian Raymer <deldotdr@gmail.com>
# 
# This module is part of codenode, and is distributed under the terms 
# of the BSD License:  http://www.opensource.org/licenses/bsd-license.php
#########################################################################

from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson as json
from django.contrib.auth.decorators import login_required

from codenode.frontend.attach.models import Storage

from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()

@login_required
def attach(request, template_name='attach/attach.html'):
    """Shows all attached files, and handles upload.
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            attachfile = Storage()
            attachfile.owner = request.user
            attachfile.normal.save(request.FILES['file'].name, request.FILES['file'])
            attachfile.save()
            return HttpResponseRedirect('/attach/?success=true')
    else:
        form = UploadFileForm()
    return render_to_response(template_name, {'form':form, 'user':request.user})
