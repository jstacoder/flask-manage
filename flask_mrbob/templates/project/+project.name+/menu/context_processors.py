# define bluepriont specific context processors

def example_context():
    return {'example':'value'}


def nav_links():
    return {'nav_links':(
                ('base.index','Home'),
                ('base.about','About'),
                ('base.index','another'),
                ('base.index','more'),
                ('base.index','contact'),
            )
    }

def nav_title():
    return {'nav_title':'My Site'}
# register this in settings.py to make it avialible in all templates
