from mrbob.configurator import Configurator,Question
import mrbob.bobexceptions as mbe

def pre_skip_question(c,q):
    if q.extra.skip:
        raise mbe.SkipQuestion

def post_skip_question(c,q,a):
    if q.extra.skip_answer == a:
        raise mbe.SkipQuestion

def set_url_prefix_default(c,q):
    q.default = c.variables.get(q.extra.get('set_to'))
    return q

def move_template_folder(c,q,a):
    return a

def set_default_db(c,q):
    q = Question('db_uri','its chosen')

def add_prefix(c,q,a):
    return a
    

def construct_db_uri(c,q):
    uri = {}
    for itm in ['db_driver','db_user','db_pw','db_host','db_port','db_name']:
        uri[itm] = c.variables['project.{}'.format(itm)]
    u ='{}://{}:{}@{}:{}/{}'.format(uri['db_driver'],uri['db_user'],uri['db_pass'],uri['db_host'],uri['db_port'],uri['db_name'])
    q.default = u
    q.question = 'Default is {}'.format(u)
    #return u


def secret_key(c,q,a):
    if a:
        import random
        chars = 'zxcvbnm,.;lkjhgfdsaqwertyuiop[]!@#$%^&*()_+=-0987654321'
        length = 50
        rtn = ''
        for x in range(length):
            rtn += str(random.choice(chars))
    else:
        rtn = 'A Secret Shhh'

    return rtn

move_template_dir = move_template_folder

def add_blueprints(c):
    c.variables['blueprints'] = []

