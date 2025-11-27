import oracledb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

path_to_instant_client = r"D:\oracle\instantclient_23_0"

try:
    oracledb.init_oracle_client(lib_dir=path_to_instant_client)
    
except Exception as e:
    print(f"Erro ao iniciar Oracle Client: {e}")
    print("Verifique se o caminho da pasta está correto e se baixou a versão x64.")

# SEUS DADOS
DB_USER = "THALESTADEU18_SCHEMA_T8VNF"
DB_PASSWORD = "Z9D32n1IQNU#Q0FUECOPG8V9YQ34MN"  # <--- COLOCAR SUA SENHA AQUI
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