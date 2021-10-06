from sqlalchemy import Column, Integer, String, ForeignKey, orm
from sqlalchemy_serializer import SerializerMixin

from School146.data.db_session import SqlAlchemyBase


class AlbumPicture(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'album_pictures'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    path_to_picture = Column(String)
    album_id = Column(Integer, ForeignKey('albums.id'))

    album = orm.relation('Album')