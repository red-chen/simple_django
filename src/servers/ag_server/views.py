#!/usr/bin/python
# -*- coding: utf-8 -*- 

import urllib
import logging
import string
import json

from django.http import Http404
from django.http import HttpResponse
from django.template import loader, Context
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt

from core.common.conf import *

from core.service.request_count_service import *

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return self._do(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self._do(request, *args, **kwargs)

    def _do(self, request, *args, **kwargs):
        logging.debug("Begin IndexView")
        
        service = RequestCountService()
        service.add_one()

        ret = {"Message" : "It's works !"}
        for k,v in list_all().items():
            if not (k.find('pass') >=0 or k.find('access') >=0):
                ret[k] = v
   
        c = service.get()
        ret['request_count'] = c.count

        return HttpResponse(json.dumps(ret, sort_keys=True, indent=4), content_type='application/json', status=200)

class HtmlView(View):
    def get(self, request, *args, **kwargs):
        return self._do(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self._do(request, *args, **kwargs)

    def _do(self, request, *args, **kwargs):
        logging.debug("Begin HtmlView")
        c = {}
        template = loader.get_template('index.html')
        return HttpResponse(template.render(Context(c)))
