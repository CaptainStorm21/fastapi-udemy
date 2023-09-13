from sqlalchemy import Column, Integer, String
from database import Base

class Product(Base):
    __tablename__ = 'products'
    name = Column(String)
    description= Column(String)
    price = Column(Integer)
    id = Column(Integer, primary_key = True, index = True)

class Seller(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String)
    email= Column(String)
    password = Column(String)
