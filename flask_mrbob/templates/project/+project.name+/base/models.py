# -*- coding: utf-8 -*-

"""
    base.base
"""

from flask.ext.login import UserMixin
from sqlalchemy.ext.declarative import declared_attr
#from werkzeug.security import generate_password_hash, check_password_hash
from LoginUtils import encrypt_password as generate_password_hash
from LoginUtils import check_password as check_password_hash

from ext import db
from basemodels import BaseMixin

for attr in dir(db):
    globals()[attr] = getattr(db,attr)


class User(UserMixin, BaseMixin, db.Model):
    __tablename__ = 'users'

    username = Column(String(32))
    email = Column(String(32), unique=True)
    password = Column(String(32))
    role_id = Column(Integer,ForeignKey('roles.id'))

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return u'<User %r>' % self.username

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()



class Role(BaseMixin,Model):
    __tablename__ = 'roles'

    name = Column(String(55),unique=True,nullable=False)
    users = relationship('User',backref='role')



