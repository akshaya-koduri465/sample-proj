from sqlalchemy import Column, Integer, String,Numeric,Boolean
from database import Base

class products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category=Column(String(80),nullable=False)
    name = Column(String(100), nullable=False)
    brand=Column(String(100),nullable=False)
    model = Column(String(100), nullable=False)
    price= Column(Numeric(10,2),nullable=False)


class Users(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True,index=True)
    name=Column(String(25),nullable=False)
    email=Column(String(50),unique=True,nullable=False)
    is_active=Column(Boolean,default=True,nullable=False)
    is_admin=Column(Boolean,default=False,nullable=False)
    password=Column(String(300),nullable=False)
