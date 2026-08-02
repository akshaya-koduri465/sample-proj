from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import Base, engine, SessionLocal
from fastapi import Response
from auth import verify_admin


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# @app.get("/products")
# def sample():
#     return "hello world"

# Create Product
@app.post("/products", response_model=schemas.productResponse)
def create(products: schemas.productCreate, db: Session = Depends(get_db)):
    return crud.create_products(db, products)


# Get All Products
@app.get("/products", response_model=list[schemas.productResponse])
def read_all(
    db: Session = Depends(get_db),
    user=Depends(verify_admin)
):
    return crud.get_products(db)


# Get One Product
@app.get("/products/{product_id}", response_model=schemas.productResponse)
def read_one(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)   # ✅ Correct
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


# Update Product
@app.put("/products/{product_id}", response_model=schemas.productResponse)
def update(product_id: int, product: schemas.productCreate, db: Session = Depends(get_db)):
    updated = crud.update_products(db, product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


# Delete Product
@app.delete("/products/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_product(db, product_id)   
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


# # Get Products by Brand
@app.get("/brand/{brand}")
def get_brand_emp(brand: str, db: Session = Depends(get_db)):
    return crud.get_emp_by_brand(db, brand)   




@app.post("/register_user")
def user_reg(user:schemas.UserCreate,db:Session=Depends(get_db)):
    return crud.create_user(user,db)



@app.post("/login")
def user_login(response:Response,user:schemas.UserLogin,db:Session=Depends(get_db)):
    return crud.login_user(user,db,response)