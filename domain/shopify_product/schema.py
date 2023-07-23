from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    itfcd_id: int
    product_id: int

    class Config:
        from_attributes = True

class Create(BaseModel):
    itfcd_id: int
    product_id: int

    @validator('itfcd_id', 'product_id')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int