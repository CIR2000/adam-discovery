# -*- coding: utf-8 -*-
"""
    adam-discovery.auth.py
    ~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2017 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
from eve.auth import BasicAuth


class Auth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        user = os.environ.get('WRITE_USER')
        pw = os.environ.get('WRITE_PASSWORD')
        if username is None:
            return False
        return username == user and password == pw
