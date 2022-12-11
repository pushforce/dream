from typing import List
from pydantic import BaseModel


class Sample(BaseModel):
    checked_sentence: str
    knowledge: str
    text: str


class RequestSample(Sample):
    history: str


class BatchRequest(BaseModel):
    batch: List[RequestSample]


class KgModelInput(BaseModel):
    history: List[str]
    inputs: List[Sample]
