from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    shopify_product_id: int
    shopify_collection_id: int
    collect_id: int

    class Config:
        from_attributes = True

class Create(BaseModel):
    shopify_product_id: int
    shopify_collection_id: int
    collect_id: int
    
    @validator('shopify_product_id', 'shopify_collection_id', 'collect_id')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int