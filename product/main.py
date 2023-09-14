
from .database import engine
from  fastapi import FastAPI, Response, HTTPException
from sqlalchemy.sql.functions import mode
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from .database import engine, SessionLocal
from fastapi import status
from passlib.context import CryptContext
from .routers import product
from .import schemas
from .import models

pwd_context = CryptContext(schemes = ["bcrypt"], deprecated="auto")

app = FastAPI(
    title="Products API",
    description="this is db for user and product",
    terms_of_service="http://www.google.com",
    contact={
        "Developer name": "AI",
        "Developer email": "Hooligans@yahoo.com"
    }
)

app.include_router(product.router)
models.Base.metadata.create_all(engine)


@app.post('/seller', response_model=schemas.DisplaySeller)
def create_seller(request:schemas.Seller,  db: Session = Depends(get_db)):
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(username = request.username, email = request.email, password = hashedpassword)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
