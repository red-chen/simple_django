 #!/usr/bin/env python2.7
 #-*- coding:utf-8 -*-

class ServerError(object):
    OBJECT_EXIST = "OBJECT_EXIST"

class ServerException(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
        Exception.__init__(self)

    def get_code(self):
        return self.code

    def get_message(self):
        return self.message

    def __str__(self):
        return '%s,%s'%(self.code, self.message)
