######################################################################### 
# Copyright (C) 2007, 2008, 2009 
# Alex Clemesha <alex@clemesha.org> & Dorian Raymer <deldotdr@gmail.com>
# 
# This module is part of codenode, and is distributed under the terms 
# of the BSD License:  http://www.opensource.org/licenses/bsd-license.php
#########################################################################

from django.db import models
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

storage = FileSystemStorage(location="data/attach")

# Write out a file to be used as default content
#temp_storage.save('tests/default.txt', ContentFile('default content'))

class Storage(models.Model):
    def normal_upoad_to(self, filename):
        print "SSSSSSSSSSS - normal_upload_to ", filename
        return 'foo'

    owner = models.ForeignKey(User)
    normal = models.FileField(storage=storage, upload_to=".")

