from pydantic import BaseModel

class Product(BaseModel):
    name: str
    description: str
    price: int
    
#to keep fields private
class DisplayProduct(BaseModel):
    name: str
    description: str 
    class Config:
        orm_mode = True