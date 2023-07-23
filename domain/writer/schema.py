from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    itfcd_id: int
    name: str
    description: str
    is_recent: float

    class Config:
        from_attributes = True

class Create(BaseModel):
    itfcd_id: int
    name: str
    description: str
    is_recent: float

    @validator('name', 'description')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('itfcd_id', 'is_recent')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int