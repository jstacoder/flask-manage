# -*- coding: utf-8 -*-

"""
    base.forms
    ~~~~~~~~~~

    The most common forms for the whole project.

    :copyright: (c) 2012 by Roman Semirook.
    :license: BSD, see LICENSE for more details.
"""

#from flask.ext.codemirror.fields import CodeMirrorField
from wtforms import TextField, validators, PasswordField, TextAreaField, HiddenField
from flask.ext.wtf import Form 
from wtforms.ext.sqlalchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.validators import Email, Required
from wtforms import validators, fields

