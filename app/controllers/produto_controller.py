from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import produto_service

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/")
def criar_produto(nome: str, valor: float, db: Session = Depends(get_db)):
    try:
        produto = produto_service.criar_produto(db, nome, valor)
        return produto
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)
