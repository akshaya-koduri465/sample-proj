from sqlalchemy.orm import Session
import models
import schemas

def create_products(db: Session, products: schemas.productCreate):
    #creating  a products object with user values
    db_products = models.products(**products.model_dump())
    #adding new products to existing table
    db.add(db_products)
    #commiting the changes to the database
    db.commit()
    #refreshing the database to get updated values
    db.refresh(db_products)
    #returning response to the user
    return db_products

def get_products(db: Session):
    return db.query(models.products).all() #fetch the data from products table

def get_products(db: Session, products_id: int): #if only need one product
    return db.query(models.products).filter(
        models.products.id == products_id
    ).first()

def update_products(db: Session, products_id: int, products: schemas.productCreate):
    db_products = get_products(db, products_id)
    if not db_products:
        return None
    db_products.name = products.name
    db_products.category=products.category
    db_products.brand=products.brand
    db_products.model=products.model
    db_products.price=products.price

    db.commit()
    db.refresh(db_products)
    return db_products

def delete_products(db: Session, products_id: int):
    db_products = get_products(db, products_id)
    if not db_products:
        return None
    db.delete(db_products)
    db.commit()
    return db_products



def get_prod_by_brand(db:Session,brand:str):
    print(brand)
    return db.query(models.products).filter(
        models.products.brand==brand
    ).all()

    