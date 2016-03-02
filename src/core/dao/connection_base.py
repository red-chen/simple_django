#!/usr/bin/env python2.7

import MySQLdb
from DBUtils.PooledDB import PooledDB

from core.common.conf import *
from mysqlcat.mysqlcat import *

db_pool = PooledDB(
    MySQLdb, 
    maxconnections=int(get(Conf.mysql_connection)), 
    host=get(Conf.mysql_endpoint),
    user=get(Conf.mysql_user), 
    passwd=get(Conf.mysql_pass), 
    db=get(Conf.mysql_db), 
    port=int(get(Conf.mysql_port))
)

class ConnectionBase(object):
    def __init__(self):
        pass

    def get_connection(self):
        global db_pool
        return Connection(pool = db_pool)
