from sqlalchemy import Integer, Column, String
from sqlalchemy_serializer import SerializerMixin

from School146.data.db_session import SqlAlchemyBase


class Menu(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product = Column(String)
    price = Column(Integer)
