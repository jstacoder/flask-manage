# -*- coding: utf-8 -*-

"""
    base.views
    ~~~~~~~~~~
"""

from base import base
from baseviews import BaseView
from flask import flash, redirect, request, url_for


class IndexView(BaseView):
    _template = 'index.html'

    def get(self):
        return self.render()

base.add_url_rule('', view_func=IndexView.as_view('index'))

class AboutView(BaseView):
    _template = 'about.html'

    def get(self):
        return self.render()

base.add_url_rule('/about',view_func=AboutView.as_view('about'))
