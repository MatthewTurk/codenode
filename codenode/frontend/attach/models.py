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

"""
TODO - Associate User Files with filesystem location:
-----------------------------------------------------
    1) Make sub-dirs under 'data/attach'
    the PrimaryKey (an integer) of that user, 
    e.g: 'data/attach/1' for the 1st User, etc.

    2) Make sub-dirs under 'data/attach' have
    guid's.  Need to add extra Model logic for this.

"""
#XXX How to make different Storage Strategies Pluggable?
storage = FileSystemStorage(location="data/attach") #XXX location in settings

# Write out a file to be used as default content
#temp_storage.save('tests/default.txt', ContentFile('default content'))

class AttachedFile(models.Model):
    owner = models.ForeignKey(User)
    file = models.FileField(storage=storage, upload_to=".")
