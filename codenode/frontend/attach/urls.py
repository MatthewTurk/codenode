######################################################################### 
# Copyright (C) 2007, 2008, 2009 
# Alex Clemesha <alex@clemesha.org> & Dorian Raymer <deldotdr@gmail.com>
# 
# This module is part of codenode, and is distributed under the terms 
# of the BSD License:  http://www.opensource.org/licenses/bsd-license.php
#########################################################################

from django.conf.urls.defaults import *
from codenode.frontend.attach.views import attach, delete

urlpatterns = patterns('',
    url(r'^$', attach, name='attach'),
    url(r'^delete$', delete, name='delete'),
)
