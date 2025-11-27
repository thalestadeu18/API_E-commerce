from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SEUS DADOS
DB_USER = "THALESTADEU18_SCHEMA_T8VNF"
DB_PASSWORD = "<SUA_SENHA_AQUI>"  # <--- COLOCAR SUA SENHA AQUI
DB_HOST = "db.freesql.com"
DB_PORT = "1521"
DB_SERVICE = "23ai_34ui2"

DATABASE_URL = f"oracle+oracledb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?service_name={DB_SERVICE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    
    
    
    
    db = SessionLocal()
    try:
        
        
        
        
        yield db
    finally:
        
        
        
    
        db.close()