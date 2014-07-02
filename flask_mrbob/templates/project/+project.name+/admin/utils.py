
def get_pk(obj):
    if 'id' in obj.__dict__:
        return obj.id
    raise IOError
def get_pk(obj):
    if 'id' in obj.__dict__:
        return obj.id
    raise IOError
