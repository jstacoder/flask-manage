from flask.views import MethodView
from flask.templating import render_template
from flask.helpers import url_for

class BaseView(MethodView):
    _template = None
    _form = None    
    _context = {}

    def render(self,**kwargs):
        if self._template is None:
            return NotImplemented
        if kwargs:
            self._context.update(kwargs)
        return render_template(self._template,**self._context)


class ModelView(BaseView):
    _model = None

    def add(self,**kwargs):
        tmp = self._model(**kwargs)
        tmp.save()

    def update(self,model_id,**kwargs):
        tmp = self._model.query.filter_by(self._model.id==model_id).first()
        for k in kwargs.keys():
            tmp.__dict__[k] = kwargs[k]
        tmp.save()

    def get_by_id(self,model_id):
        tmp = self._model.get_by_id(model_id)
        return tmp




