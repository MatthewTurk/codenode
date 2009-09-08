######################################################################### 
# Copyright (C) 2007, 2008, 2009 
# Alex Clemesha <alex@clemesha.org> & Dorian Raymer <deldotdr@gmail.com>
# 
# This module is part of codenode, and is distributed under the terms 
# of the BSD License:  http://www.opensource.org/licenses/bsd-license.php
#########################################################################

from django.contrib import admin

from codenode.frontend.attach.models import Storage

class StorageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Storage, StorageAdmin)

