from sqlalchemy import Column, Integer, String, Float
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True, nullable=False)
    valor = Column(Float, nullable=False)
    descricao = Column(String, nullable=True) 
    quantidade = Column(Integer, default=0)