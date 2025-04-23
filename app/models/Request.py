from pydantic import BaseModel
from typing import Optional

class RequestData(BaseModel):
    model: str
    body: str
    stream: Optional[bool] = False
    temperature: Optional[float] = 0.8