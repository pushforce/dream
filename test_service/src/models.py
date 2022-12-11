from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.dialects.postgresql import JSONB

from db import Base


class Process(Base):
    __tablename__ = 'process'

    id = Column(Integer, Identity(increment=True), primary_key=True)
    service = Column(String(128))
    endpoint = Column(String(128))
    input = Column(JSONB)
    output = Column(JSONB)
