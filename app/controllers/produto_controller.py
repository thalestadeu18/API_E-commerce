from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import produto_service

router = APIRouter(prefix="/produtos", tags=["Catálogo de E-commerce"])

@router.post("/")
def criar_produto(
    nome: str, 
    valor: float, 
    descricao: str, 
    quantidade: int, 
    db: Session = Depends(get_db)
):
    try:
        # Chama o serviço passando todos os dados
        produto = produto_service.criar_produto(db, nome, valor, descricao, quantidade)
        return produto
    except ValueError as e:
        # Tratamento de exceção com status 400 (Bad Request)
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)