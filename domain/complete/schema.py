from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    itfcd_id: int
    is_booksen: int
    is_product: int
    is_image: int
    is_weight: int
    is_price: int
    is_stock: int
    is_variant: int

    class Config:
        from_attributes = True

class Create(BaseModel):
    itfcd_id: int
    is_booksen: int
    is_product: int
    is_image: int
    is_weight: int
    is_price: int
    is_stock: int
    is_variant: int

    @validator('itfcd_id')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int

class Count(BaseModel):
    count: int