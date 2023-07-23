from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    category_rank: int
    category_code: int
    category_name: str
    top_category_code: int

    class Config:
        from_attributes = True

class Create(BaseModel):
    category_rank: int
    category_code: int
    category_name: str
    top_category_code: int

    @validator('category_name')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v

    @validator('category_rank', 'category_code')
    def not_zero(cls, v):
        if v == 0:
            raise ValueError('0은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int