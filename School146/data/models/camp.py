from sqlalchemy import Column, Integer, String
from sqlalchemy_serializer import SerializerMixin

from School146.data.db_session import SqlAlchemyBase


class Camp(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'camp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String)
    pictures = Column(String)