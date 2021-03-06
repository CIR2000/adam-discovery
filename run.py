# -*- coding: utf-8 -*-
"""
    adam-discovery.run.py
    ~~~~~~~~~~~~~~~~~~~~~

    The API launch script.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os

from eve import Eve
from auth import Auth
# from discovery.oauth2 import BearerAuth

# Load the settings file using a robust path so it works when
# the script is imported from the test suite.
this_directory = os.path.dirname(os.path.realpath(__file__))
settings_file = os.path.join(this_directory, 'settings.py')

port = os.environ.get('PORT')
if port:
    # Heroku
    host = '0.0.0.0'
    port = int(port)
else:
    host = '127.0.0.1'
    port = 9000

app = Eve(settings=settings_file, auth=Auth)

if __name__ == '__main__':
    app.run(host=host, port=port)
