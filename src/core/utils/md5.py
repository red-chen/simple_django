#!/usr/bin/env python2.7

import md5

class Md5(object):
    def __init__(self, input_str):
        self.m = md5.new()
        self.input_str = input_str

    def __str__(self):
        return m.hexdigest()

