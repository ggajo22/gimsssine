from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    itfcd_id: int
    status: str
    price_sale: float
    name: str
    useruse1: str
    useruse2: str
    price: float
    opndate: str
    outrt2: int
    qty: int
    retyn: str
    cover_image_url: str
    cover_image_url2: str
    desc_table: str
    desc_pub: str
    booxen_cate_cd1: int
    booxen_cate_cd2: int
    booxen_cate_cd3: int

    class Config:
        from_attributes = True

class Create(BaseModel):
    itfcd_id: int
    status: str
    price_sale: float
    name: str
    useruse1: str
    useruse2: str
    price: float
    opndate: str
    outrt2: int
    qty: int
    retyn: str
    cover_image_url: str
    cover_image_url2: str
    desc_table: str
    desc_pub: str
    booxen_cate_cd1: int
    booxen_cate_cd2: int
    booxen_cate_cd3: int

    @validator('status', 'name', 'useruse1', 'useruse2')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('itfcd_id', 'price_sale', 'price')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int