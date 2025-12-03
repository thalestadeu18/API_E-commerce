from sqlalchemy.orm import Session
from models.produto_model import Produto

def criar_produto(db: Session, nome: str, valor: float):

    # verifica se existe produto com mesmo nome
    produto_existente = db.query(Produto).filter(Produto.nome == nome).first()

    if produto_existente:
        raise ValueError("Produto existente!")

    # criar produto
    novo_produto = Produto(nome=nome, valor=valor)
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(Produto).all()
