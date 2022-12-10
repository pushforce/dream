from typing import List
from pydantic import BaseModel


class Payload(BaseModel):
    sentences: List[str]


class ProcessCreate(BaseModel):
    service: str
    endpoint: str
    payload: Payload
