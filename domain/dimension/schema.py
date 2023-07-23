from typing import Optional
from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    itfcd_id: int
    weight: float
    page_cnt: int
    dim1: float
    dim2: float
    dim3: float

    class Config:
        from_attributes = True

class Create(BaseModel):
    itfcd_id: int
    weight: float
    page_cnt: int
    dim1: float
    dim2: float
    dim3: float

    @validator('itfcd_id', 'weight', 'page_cnt', 'dim1', 'dim2', 'dim3')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int