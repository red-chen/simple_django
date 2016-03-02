#!/usr/bin/env python2.7

import logging
import json

class Conf(object):
    # mysql
    mysql_endpoint = 'mysql_endpoint'
    mysql_port = 'mysql_port'
    mysql_user = 'mysql_user'
    mysql_pass = 'mysql_pass'
    mysql_db = 'mysql_db'
    mysql_connection = 'mysql_connection'
    mysql_table_prefix = 'mysql_table_prefix'

    def __init__(self):
        self.kv = {}

        # global flag define
        self.kv['default_server_name'] = "my_server"
        self.kv['other_global_flag'] = "other"
        self.kv[Conf.mysql_endpoint] = 'localhost'
        self.kv[Conf.mysql_port] = '3306'
        self.kv[Conf.mysql_user] = 'root'
        self.kv[Conf.mysql_pass] = '123456'
        self.kv[Conf.mysql_db] = 'test'
        self.kv[Conf.mysql_connection] = 50
        self.kv[Conf.mysql_table_prefix] = 'simple_django'

#########################################################
#########################################################

_g_conf = None
if _g_conf == None:
    _g_conf = Conf()

def load(conf_path):
    global _g_conf
    with open(conf_path) as fp:
        jj = json.load(fp)
        for k,v in jj.items():
            if _g_conf.kv.has_key(k):
                _g_conf.kv[k]  = v
    logging.info('load the config:' + conf_path)
    logging.info('{')
    for k,v in _g_conf.kv.items():
        logging.info('    %s : %s'%(k, v))
    logging.info('}')

def get(key):
    global _g_conf
    return _g_conf.kv[key]

def list_all():
    global _g_conf
    return _g_conf.kv
