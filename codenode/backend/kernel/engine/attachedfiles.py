######################################################################### 
# Copyright (C) 2007, 2008, 2009 
# Alex Clemesha <alex@clemesha.org> & Dorian Raymer <deldotdr@gmail.com>
# 
# This module is part of codenode, and is distributed under the terms 
# of the BSD License:  http://www.opensource.org/licenses/bsd-license.php
#########################################################################

import os
#from django.contrib.auth.models import User
#from codenode.frontend.attach.models import AttachedFile


#TODO:
"""
- Make this functionality "MIDDLEWARE"

- Update User file listing by attaching 
'Events' to actions like 'Upoad/Delete/Modify'.

- Document what the special imported
variable is called, i.e. 'FILES', and usage.

"""

class UsersAttachedFiles(object):
    """Represents all Attached files by a given User.

    Imported into a running ``namespace`` of a User's
    ``Notebook`` for easy access to all Attached files.
    """
    #def __init__(self, ownerid=None, rootdir="./static/data"):
    #    _files = AttachedFile.objects.filter(owner__id=ownerid)
    #    self.files = [obj.file.name.split("/")[-1] for obj in _files]
    def __init__(self, ownerid=None, rootdir="../attach"):
        self.ownerid = ownerid
        self.rootdir = rootdir

    def _get_userfiles(self):
        return os.listdir(self.rootdir)

    def __repr__(self):
        userfiles = self._get_userfiles()
        return str(userfiles)

    def __getitem__(self, item):
        userfiles = self._get_userfiles()
        if item in userfiles:
            filepath = os.path.join(self.rootdir, item)
            return open(filepath, 'r')
        else:
            return "No file '%s' exists." % item
