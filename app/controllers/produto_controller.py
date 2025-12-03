from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import produto_service

router = APIRouter(prefix="/produtos", tags=["Catálogo de E-commerce"])

@router.post("/{nome}/{valor}/{quantidade}")#Daniel:alterei a rota para conseguimos adcionar produtos pelo gitbash
def criar_produto(
    nome: str, 
    valor: float, 
    descricao: str, 
    quantidade: int, 
    db: Session = Depends(get_db)
):
    try:
        produto = produto_service.criar_produto(db, nome, valor, descricao, quantidade)
        return produto
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):

    return produto_service.listar_produtos(db)
#Daniel:isso e para deletar pelo gitbash rota:curl -X DELETE http://127.0.0.1:8000/produtos/{poduto_id}
@router.delete("/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    sucesso = produto_service.deletar_produto(db, produto_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}
