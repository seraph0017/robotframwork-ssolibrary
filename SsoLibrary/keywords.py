#!/usr/bin/env python
#encoding:utf-8
import os
import sys
PATH = os.path.abspath(__file__)
genpy_path = os.path.join(os.path.split(PATH)[0],'..','genpy')
sys.path.append(genpy_path)
import robot

from robot.libraries.BuiltIn import BuiltIn
from SSO import SsoService
from SSO.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from nose.tools import assert_equal


class SsoKeywords(object):

    def __init__(self):
        self._cache = robot.utils.ConnectionCache('No sessions created')
        self.builtin = BuiltIn()


    def create_session(self,client_alias,transport_alias,host,port):
        transport = TSocket.TSocket(host,int(port))
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = SsoService.Client(protocol)
        transport.open()
        self._cache.register(client,client_alias)
        self._cache.register(transport,transport_alias)


    def delete_all_session(self):
        self._cache.empty_cache()


    def login(self,client_alias,username,password,project_id):
        client = self._cache.switch(client_alias)
        resp = client.Login(username,password,project_id)
        assert_equal(resp.error_code,200,resp)
        return resp








