from typing import Optional
from pydantic import BaseModel


class RequestBodyAdd(BaseModel):
    request_id: str
    user: str
    item: str
    trigger_error: Optional[str] = None


class RequestBodyDelete(BaseModel):
    request_id: str
    user: str
    item: str
    trigger_error: Optional[str] = None


class RequestBodyList(BaseModel):
    request_id: str
    user: str
    trigger_error: Optional[str] = None


class RequestBodyMark(BaseModel):
    request_id: str
    user: str
    item: str
    trigger_error: Optional[str] = None