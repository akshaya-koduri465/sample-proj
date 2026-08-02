from sqlalchemy.orm import Session
import models
import schemas
import bcrypt
from fastapi import Response

from datetime import datetime,timedelta
import jwt


SECRET_KEY = "abcdefghijklmnopqrstuvwxyz"
ALGORITHM = "HS256"


# Create Product
def create_products(db: Session, products: schemas.productCreate):
    db_products = models.products(**products.model_dump())
    hashed=bcrypt.hashpw(db_products.password.encode(),bcrypt.gensalt(rounds=13).decode("utf-8"))
    db.add(db_products)
    db.commit()
    db.refresh(db_products)

    return db_products


# Get All Products
def get_products(db: Session):
    return db.query(models.products).all()


# Get One Product by ID
def get_product(db: Session, products_id: int):
    return db.query(models.products).filter(
        models.products.id == products_id
    ).first()


# Update Product
def update_products(db: Session, products_id: int, products: schemas.productCreate):
    db_products = get_product(db, products_id)

    if not db_products:
        return None

    db_products.name = products.name
    db_products.category = products.category
    db_products.brand = products.brand
    db_products.model = products.model
    db_products.price = products.price

    db.commit()
    db.refresh(db_products)

    return db_products


# Delete Product
def delete_product(db: Session, products_id: int):
    db_products = get_product(db, products_id)

    if not db_products:
        return None

    db.delete(db_products)
    db.commit()

    return db_products


# Get Products by Brand
def get_emp_by_brand(db: Session, brand: str):
    return db.query(models.products).filter(
        models.products.brand == brand
    ).all()


def create_user(user:schemas.UserCreate,db:Session):
    new_user=models.Users(**user.model_dump())
    hashed=bcrypt.hashpw(new_user.password.encode(),bcrypt.gensalt(rounds=12)).decode()
    new_user.password=hashed
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user




def login_user(user: schemas.UserLogin, db: Session, response: Response):
    is_exists = db.query(models.Users).filter(
        models.Users.email == user.email
    ).first()

    if not is_exists:
        return {"message": "user not found"}

    valid = bcrypt.checkpw(
        user.password.encode(),
        is_exists.password.encode()
    )

    if not valid:
        return {"message": "invalid password"}

    payload = {
        "name": is_exists.name,
        "email": is_exists.email,
        "is_admin": is_exists.is_admin,
        "is_loggedin":True,
        "exp": datetime.utcnow() + timedelta(seconds=10)
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    # Store token in cookie
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True
    )

    return {
        "message": "login successful",
        "access_token": token
    }
