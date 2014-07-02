# -*- coding: utf-8 -*-

"""
"""

from flask.templating import render_template
from flask.views import MethodView
from admin import admin


class AdminDashboardView(MethodView):

    def get(self):
        from auth.models import AccessToken
        tokens = AccessToken.query.all()
        return render_template('dashboard.html',tokens=tokens)

admin.add_url_rule('', view_func=AdminDashboardView.as_view('main'))
