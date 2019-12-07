import uuid

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import (
    String,
)
from sqlalchemy.ext.declarative.api import declarative_base


Base = declarative_base()


class BaseWithUUID(Base):
    id = Column(String, primary_key=True, default=uuid.uuid1)


class Dog(BaseWithUUID):
    __tablename__ = 'dogs'

    breed = Column(String, unique=True)
