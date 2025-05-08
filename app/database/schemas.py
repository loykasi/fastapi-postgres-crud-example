from pydantic import BaseModel

class BookBase(BaseModel):
    id: int
    title: str

class BookPut(BaseModel):
    title: str
        
class StudentBase(BaseModel):
    cccd: str
    name: str
    phone: str

class StudentPut(BaseModel):
    name: str
    phone: str