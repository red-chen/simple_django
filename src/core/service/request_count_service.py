#!/usr/bin/env python2.7

import logging
import MySQLdb

from core.common.server_exception import *

from core.dao.request_count_dao import *

class RequestCountService(object):
    def __init__(self):
        self.dao = RequestCountDao()

    def create_table(self, check_not_exist=False):
        try:
            self.dao.create_table(check_not_exist)
        except MySQLdb.Error, e:
            logging.error('Mysql error, %s, %s'%(e.args[0], e.args[1]))
            if int(e.args[0]) == 1050:
                raise ServerException(ServerError.OBJECT_EXIST, e.args[1])
            else:
                raise ServerException((ServerError.ERROR, e.args[1]))
 
    def add_one(self):
        try:
            self.dao.add_one()
        except MySQLdb.Error, e:
            logging.error('Mysql error, %s, %s'%(e.args[0], e.args[1]))
            raise ServerException(str(e.args[0]), e.args[1])
     
    def get(self):
        try:
            return self.dao.get()
        except MySQLdb.Error, e:
            logging.error('Mysql error, %s, %s'%(e.args[0], e.args[1]))
            raise ServerException(str(e.args[0]), e.args[1])
  
