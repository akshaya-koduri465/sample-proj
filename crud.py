from sqlalchemy.orm import Session
import models
import schemas


# Create Product
def create_products(db: Session, products: schemas.productCreate):
    db_products = models.products(**products.model_dump())
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