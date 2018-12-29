from datetime import datetime

from db import pg_db as db
from playhouse.postgres_ext import Model, CharField, TextField, ForeignKeyField, DateTimeField


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class Tag(BaseModel):
    name = CharField(unique=True, verbose_name="name")
    desc = CharField(verbose_name="description")


class Article(BaseModel):
    title = CharField(unique=True, verbose_name="title")
    content = TextField(verbose_name="content")
    tag = ForeignKeyField(Tag, related_name="articles", verbose_name="tag")
    create_time = DateTimeField(default=datetime.now, verbose_name="create time")
    up_time = DateTimeField(default=datetime.now, verbose_name="create time")


if __name__ == '__main__':
    db.connect()
    db.create_tables([Article, Tag])
