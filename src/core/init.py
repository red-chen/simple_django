# !/usr/bin/env python2.7
# -*- cooding:utf-8 -*-

import logging
import logging.config
import core.common.conf

from core.service.request_count_service import *

def init_check_mysql():
    logging.info("begin init_check_mysql")
    request_count_service = RequestCountService()
    request_count_service.create_table(check_not_exist=True)
    request_count_service.add_one()
    logging.info("end init_check_mysql")
  

def init_check():
    init_check_mysql()

# server main
def load():
    # load config
    logging.config.fileConfig('conf/logging.conf')
    core.common.conf.load('conf/conf.json')

    # check
    init_check() 



