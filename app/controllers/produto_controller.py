from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import produto_service
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/produtos", tags=["Catálogo de E-commerce"])

# Criar produto
@router.post("/{nome}/{valor}/{quantidade}")  # Daniel: alterei a rota para conseguir adicionar produtos pelo Git Bash
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


# Listar produtos
@router.get("/")
def listar_produtos(db: Session = Depends(get_db)):
    return produto_service.listar_produtos(db)


# Deletar produto
@router.delete("/{produto_id}")  # Daniel: rota para deletar pelo Git Bash
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    sucesso = produto_service.deletar_produto(db, produto_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"detail": "Produto deletado com sucesso"}


class ProdutoUpdate(BaseModel):
    nome: Optional[str] = None
    valor: Optional[float] = None
    descricao: Optional[str] = None

class EstoqueUpdate(BaseModel):
    quantidade_vendida: int

# Buscar produto por ID
@router.get("/{produto_id}/detalhes")
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = produto_service.buscar_produto_por_id(db, produto_id)
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# Buscar produtos por nome

@router.get("/busca/{termo}")
def buscar_produtos(termo: str, db: Session = Depends(get_db)):
    produtos = produto_service.buscar_produtos_por_nome(db, termo)
    if not produtos:
        raise HTTPException(status_code=404, detail="Nenhum produto encontrado")
    return produtos
    
# Atualizar produto
@router.patch("/{produto_id}")
def atualizar_produto(produto_id: int, dados: ProdutoUpdate, db: Session = Depends(get_db)):
    produto = produto_service.atualizar_produto(
        db,
        produto_id,
        nome=dados.nome,
        valor=dados.valor,
        descricao=dados.descricao
    )
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

# Atualizar estoque

@router.patch("/{produto_id}/estoque")
def atualizar_estoque(produto_id: int, dados: EstoqueUpdate, db: Session = Depends(get_db)):
    try:
        produto = produto_service.atualizar_estoque(db, produto_id, dados.quantidade_vendida)
        return produto
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
