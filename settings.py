# -*- coding: utf-8 -*-
"""
    adam.settings
    ~~~~~~~~~~~~~

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
import os
import discovery.domain as domain
import urllib

# Sensible settings are retrieved from environment variables when available in
# the hosting environment, or set to default values for local testing.
if os.environ.get('TESTING') is None:
    user = os.environ.get('MONGO_USERNAME')
    if user:
        pw = urllib.parse.quote_plus(os.environ.get('MONGO_PASSWORD'))
        auth = '%s:%s@' % (user, pw)
    else:
        auth = ''
    uri = os.environ.get('MONGO_URI', 'localhost:27017/adam-discovery')
    MONGO_URI = "mongodb://%s%s" % (auth, uri)
else:
    # Load MONGO settings from test suite.
    # Have to split into two lines in order to get the flake8 noqa tag in
    from tests import MONGO_DBNAME, MONGO_USERNAME, MONGO_PASSWORD  # noqa
    from tests import MONGO_HOST, MONGO_PORT # noqa

# $PORT is defined if we are hosted and likely to be in production.
if os.environ.get('PORT') is None:
    DEBUG = True

# Allow full range of CRUD operations on resources and items
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

# API is open to public read-only access.
PUBLIC_METHODS = ['GET']
PUBLIC_ITEM_METHODS = ['GET']

# Disable HATEOAS
HATEOAS = False

# We don't want pagination enabled.
PAGINATION = False

# We want the whole document back with POST/PATCH/PUT responses.
BANDWIDTH_SAVER = False

# Enable server information at the API homepage
INFO = '_info'

# Set the API domain
DOMAIN = domain.DOMAIN
