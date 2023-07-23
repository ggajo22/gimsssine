from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    booksen_category_id: int
    collection_id: int
    collection_name: str

    class Config:
        from_attributes = True

class Create(BaseModel):
    booksen_category_id: int
    collection_id: int
    collection_name: str

    @validator('collection_name')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
    @validator('collection_id')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int