from sqlalchemy import  MetaData, create_engine
from sqlalchemy.orm import sessionmaker
import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='', database='het')

# SQLAlchemy setup
engine = create_engine('mysql+mysqlconnector://', creator=lambda: conn)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
meta = MetaData()
get_db = conn.connect()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

print("connection succesfully created!")