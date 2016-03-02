#/!usr/bin/env python2.7
#-*- coding:utf-8 -*-

from core.domain.request_count import *

from core.dao.connection_base import *

from core.common.conf import *

class RequestCountDao(object):
    table_name = get(Conf.mysql_table_prefix) + '_request_table'
    def __init__(self):
        self.conn = ConnectionBase().get_connection()

    def create_table(self, check_not_exist=False):
        self.conn.begin()
        if not check_not_exist:
            self.conn.write('CREATE TABLE %s (id bigint, count bigint) ENGINE=InnoDB DEFAULT CHARSET=utf8;'%(RequestCountDao.table_name))
        else:
            self.conn.write('CREATE TABLE IF NOT EXISTS %s (id bigint, count bigint) ENGINE=InnoDB DEFAULT CHARSET=utf8;'%(RequestCountDao.table_name))
        self.conn.commit()

    def add_one(self):
        self.conn.begin()
        rows = self.conn.read("SELECT * from %s where id = 0;"%(RequestCountDao.table_name))
        count = 0
        if len(rows) <= 0:
            count = 1
            sql = "INSERT INTO "+ RequestCountDao.table_name +" values(%s, %s);"
            self.conn.write(sql, (0, int(count)))
        else:
            count = rows[0]['count'] + 1
            sql = "UPDATE "+ RequestCountDao.table_name +" SET count=%s where id = 0;"
            self.conn.write(sql, (count))
        self.conn.commit()

    def get(self):
        rows = self.conn.read("SELECT * from %s where id = 0;"%(RequestCountDao.table_name))
        if len(rows) <= 0:
            return None
        else:
            c = RequestCount()
            c.count = int(rows[0]['count'])
            return c
        
        
