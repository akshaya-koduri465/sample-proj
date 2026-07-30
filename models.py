from sqlalchemy import Column, Integer, String,Numeric
from database import Base

class products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category=Column(String(80),nullable=False)
    name = Column(String(100), nullable=False)
    brand=Column(String(100),nullable=False)
    model = Column(String(100), nullable=False)
    price= Column(Numeric(10,2),nullable=False)
    
