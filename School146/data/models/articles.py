from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

from School146.data.db_session import SqlAlchemyBase


class Article(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    text = Column(String)
    picture = Column(String)