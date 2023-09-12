from  fastapi import FastAPI
#from .import schemas
#from .import models
#from .database import engine
import models
from database import engine
import schemas
from database import SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

@app.delete('/product/{id}')
def delete(id, db: Session = Depends(get_db)):
    db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Entry Deleted'}




@app.get('/products')
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products

@app.get('/product/{id}')
def product(id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    return product

@app.post('/product')
def add(request: schemas.Product, db: Session = Depends(get_db) ): 
    new_product = models.Product(name = request.name, description = request.description, price = request.price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return request

