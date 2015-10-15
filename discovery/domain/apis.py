# -*- coding: utf-8 -*-
"""
    discovery.domain.apis.py
    ~~~~~~~~~~~~~~~~~~~~~~~~

    'apis' resource and schema settings.

    :copyright: (c) 2015 by Nicola Iarocci and CIR2000.
    :license: BSD, see LICENSE for more details.
"""
_schema = {
    'name': {
        'type': 'string',
        'required': True,
    },
    'title': {
        'type': 'string',
    },
    'description': {
        'type': 'string',
    },
    'owner': {
        'type': 'dict',
        'schema': {
            'name': {'type': 'string', 'required': True},
            'uri': {'type': 'string'},
            'contact': {'type': 'string'}
        }
    },
    'kind': {
        'type': 'string',
        'required': True,
        'allowed': ['Authentication', 'Discovery', 'UserData']
    },
    'services': {
        'type': 'list',
        'required': True,
        'schema': {
            'type': 'dict',
            'schema': {
                'base_address': {
                    'type': 'string',
                    'required': True
                },
                'status': {
                    'type': 'string',
                    'default': 'Undetermined',
                    'allowed': ['Active', 'Inactive', 'Suspended',
                                'Undetermined']
                },
                'documentation': {'type': 'string'},
                'version': {
                    'type': 'dict',
                    'default': {'major': 0, 'minor': 0, 'build': 1},
                    'schema': {
                        'major': {'type': 'integer', 'required': True},
                        'minor': {'type': 'integer', 'default': 0},
                        'build': {'type': 'integer', 'default': 0}
                    }
                },
                'deprecated': {'type': 'boolean', 'default': False},
                'discovery': {'type': 'string'},
                'authentication': {
                    'type': 'string',
                    'required': True,
                    'allowed': ['BearerToken', 'Basic', 'None'],
                }
            }
        }
    }

}

url = 'apis'

definition = {
    'url': url,
    'schema': _schema,
}
