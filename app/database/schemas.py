from pydantic import BaseModel

class PostBase(BaseModel):
    id: int
    title: str
        
class StudentBase(BaseModel):
    cccd: str
    name: str
    phone: str

class StudentPut(BaseModel):
    name: str
    phone: str