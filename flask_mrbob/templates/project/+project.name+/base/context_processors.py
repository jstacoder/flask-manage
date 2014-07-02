# -*- coding: utf-8 -*-

"""
    base.context_processors
    ~~~~~~~~~~~~~~~~~~~~~~~

    The most common context processors
    for the whole project.

"""

from flask.helpers import url_for


def common_context():
    return {            
            'my_email': 'kyle@level2designs.com',
            'type':type,
            'dir':dir,
            }


def common_forms():
    return {}
