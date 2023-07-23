from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    shopify_variant_id: int
    sales_price: float

    class Config:
        from_attributes = True

class Create(BaseModel):
    shopify_variant_id: int
    sales_price: float
    
    @validator('shopify_variant_id', 'sales_price')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int