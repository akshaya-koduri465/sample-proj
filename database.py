from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = "mysql+pymysql://root:akshaya@localhost:3306/products_db"
DATABASE_URL = mysql+pymysql://avnadmin:AVNS_kJIbgT5xyVTBGDKGX_V@mysqldb-python-backend.d.aivencloud.com:26537/defaultdb

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
