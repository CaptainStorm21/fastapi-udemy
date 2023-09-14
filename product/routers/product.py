from  fastapi import APIRouter
from fastapi import  Response, HTTPException, FastAPI
from sqlalchemy.orm import Session
from fastapi.params import Depends
from database import get_db
import models, schemas
from typing import List
from fastapi import status 

router = APIRouter()

@router.delete('/product/{id}', tags = ['products to be deleted'])
def delete(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Entry Deleted'}

@router.put('/product/{id}', tags = ['update products'])
def update(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass 
    product.update(request.dict())
    db.commit()
    return {'Product was updated'
}

@router.get('/products', response_model= List[schemas.DisplayProduct], tags=['get a list of all products'])
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@router.get('/product/{id}', response_model=schemas.DisplayProduct)
def product(id, response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'Product not found')
    return product

@router.post('/product', status_code = status.HTTP_201_CREATED)
def add(request: schemas.Product, db: Session = Depends(get_db) ): 
    new_product = models.Product(name = request.name, description = request.description, price = request.price, seller_id=1)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request
