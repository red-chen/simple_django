#!/usr/bin/env python2.7

import time

def int_to_string_localtime(second_time, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.localtime(float(second_time)))

def int_to_string_utctime(second_time, format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.gmtime(float(second_time)))

def localtime_to_int_time(str_time, format='%Y-%m-%d %H:%M:%S'):
    return int(time.mktime(time.strptime(str_time,format)))

def utctime_to_int_time(str_time, format='%Y-%m-%d %H:%M:%S'):
    return calendar.timegm(time.strptime(str_time,format))
