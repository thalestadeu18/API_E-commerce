from sqlalchemy.orm import Session
from models.produto_model import Produto

def criar_produto(db: Session, nome: str, valor: float, descricao: str, quantidade: int):

    produto_existente = db.query(Produto).filter(Produto.nome == nome).first()

    if produto_existente:
        raise ValueError("Produto já cadastrado no estoque!")

    novo_produto = Produto(
        nome=nome, 
        valor=valor, 
        descricao=descricao, 
        quantidade=quantidade
    )
    
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto

def listar_produtos(db: Session):
    return db.query(Produto).all()
    
#Daniel: Função para deletar produto
def deletar_produto(db, produto_id: int):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        return False
    db.delete(produto)
    db.commit()
    return True

