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

from codenode.frontend.attach.models import AttachedFile
from codenode.frontend.attach.forms import UploadFileForm

@login_required
def attach(request, template_name='attach/attach.html'):
    """Shows all attached files, and handles upload.
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            storage = AttachedFile()
            storage.owner = request.user
            filename = request.FILES['file'].name
            storage.file.save(filename, request.FILES['file'])
            storage.save()
            return HttpResponseRedirect('/attach/?success=upload')
    else:
        form = UploadFileForm()
        userfiles = AttachedFile.objects.filter(owner=request.user)
    return render_to_response(template_name, {'form':form, 'userfiles':userfiles, 'user':request.user})

@login_required
def delete(request):
    """Delete selected attached files.
    """
    print request.POST, request.GET # dir(request.POST)
    if request.method == 'POST':
        pass
    return HttpResponseRedirect('/attach/?success=delete')
 
