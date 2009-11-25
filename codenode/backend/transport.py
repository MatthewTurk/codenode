######################################################################### 
# Copyright (C) 2007, 2008, 2009 
# Matthew Turk <matthewturk@gmail.com>
# 
# This module is part of codenode, and is distributed under the terms 
# of the BSD License:  http://www.opensource.org/licenses/bsd-license.php
#########################################################################

"""
A simple payload mechanism, where a shared queue can be imported by any code
running in the engine.  The Interpreter is responsible for flushing this queue
and returning the values to the async notebook frontend.

"""
import pickle

class CodeNodePayload(object):
    def __init__(self, descr, mime_type, value):
        self.descr = descr # optional, for a description or 'alt text'
        self.mime_type = mime_type
        self.value = value

class CodeNodePayloadQueue(object):
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        self = object.__new__(cls, *args, **kwargs)
        self.__dict__ = cls._shared_state
        return self

    def __init__(self):
        self.queue = []

    def append(self, item):
        s = cPickle.dumps(item)
        self.queue.append(s)

    def flush(self):
        q = self.queue
        self.queue = []
        return q

    def pop(self):
        return self.queue.pop()
