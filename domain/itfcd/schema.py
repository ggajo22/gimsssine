from pydantic import BaseModel, validator

class Item(BaseModel):
    id: int
    itfcd: str

    class Config:
        from_attributes = True

class Create(BaseModel):
    itfcd: str

    @validator('itfcd')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v
    
class Update(Create):
    id: int

class Delete(BaseModel):
    id: int

class Count(BaseModel):
    count: int