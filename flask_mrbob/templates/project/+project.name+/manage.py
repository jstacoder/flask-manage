#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    manage
    ~~~~~~
"""
import subprocess
from flask.ext.script import Shell, Manager, prompt_bool
from app import app
from base.models import User
from ext import db

manager = Manager(app)

@manager.command
def clean_pyc():
    """Removes all *.pyc files from the project folder"""
    clean_command = "find . -name *.pyc -delete".split()
    subprocess.call(clean_command)


@manager.command
def init_data():
    """Fish data for project"""
    if prompt_bool('Do you want to kill your db?'):
        db.drop_all()
    try:
       db.create_all()
    except:
        pass

    user = User.query.filter(User.email=='kyle@level2designs.com').first()
    if user is None:
       user = User(username='Kyle Roux', email='kyle@level2designs.com', password='14wp88')
    user.save()


manager.add_command('shell', Shell(make_context=lambda:{'app': app, 'db': db}))


if __name__ == '__main__':
    manager.run()
