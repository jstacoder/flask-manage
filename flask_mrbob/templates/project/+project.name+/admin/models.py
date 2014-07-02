from basemodels import BaseMixin
from LoginUtils import check_password, encrypt_password
from ext import db

for attr in dir(db):
    globals()[attr] = getattr(db,attr)

class SiteUser(BaseMixin,Model):
    __tablename__ = 'site_users'

    first_name = Column(String(55))
    last_name = Column(String(55))

    username = Column(String(255),unique=True)
    date_added = Column(DateTime,default=func.now())
    _pw_hash = Column(Text)


    def __init__(self,*args,**kwargs):
        super(SiteUser,self).__init__(*args,**kwargs)
        

    def __str__(self):
        return self.username

    @property
    def pw_hash(self):
        return self._pw_hash

    @pw_hash.setter
    def pw_set(self,pw):
        self._pw_hash = encrypt_password(pw)

    def check_password(self,pw):
        return check_password(pw,self.pw_hash)

