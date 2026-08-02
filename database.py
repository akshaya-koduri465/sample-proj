from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
import os
#DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_kJIbgT5xyVTBGDKGX_V@mysqldb-python-backend.d.aivencloud.com:26537/defaultdb"
#DATABASE_URL = "mysql+pymysql://root:akshaya@localhost:3306/products_db"
load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
