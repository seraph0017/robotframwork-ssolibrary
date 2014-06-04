#!/usr/bin/env python
#encoding:utf-8
from keywords import SsoKeywords
from version import VERSION


_version_ = VERSION

class SsoLibrary(SsoKeywords):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
