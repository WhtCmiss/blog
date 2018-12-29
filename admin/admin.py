from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
from wtforms import TextAreaField
from wtforms.widgets import TextArea

from app import app
from articles.models import Article, Tag

admin = Admin(app, name='blog', template_mode='bootstrap3')


class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()


class MessageAdmin(ModelView):
    extra_js = ['//cdn.ckeditor.com/4.6.0/standard/ckeditor.js']

    form_overrides = {
        'content': CKTextAreaField
    }


admin.add_view(MessageAdmin(Article))
admin.add_view(ModelView(Tag))
