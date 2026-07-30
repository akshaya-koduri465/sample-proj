from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()






@app.post("/products", response_model=schemas.productResponse)
def create(products: schemas.productCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, products)

@app.get("/products", response_model=list[schemas.productResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.productResponse)
def read_one(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    return product

@app.put("/products/{product_id}", response_model=schemas.productResponse)
def update(products_id: int, product: schemas.productCreate, db: Session = Depends(get_db)):
    updated = crud.update_products(db, products_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="product not found")
    return updated

@app.delete("/products/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="product not found")
    return {"message":"product deleted successfully"}




@app.get("/brand/{brand}")
def get_brand_emp(brand:str,db:Session=Depends(get_db)):
    return crud.get_emp_by_brand(db,brand)