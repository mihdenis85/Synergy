from sqlalchemy import Column, Integer, String, orm
from sqlalchemy_serializer import SerializerMixin

from School146.data.db_session import SqlAlchemyBase


class Album(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)

    pictures = orm.relation('Picture', back_populates='album')