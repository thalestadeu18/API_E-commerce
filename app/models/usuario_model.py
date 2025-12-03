from sqlalchemy import Column, Integer, String
from database import Base


class usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    CPF = Column(String(11), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(10), unique=True, nullable=False)
