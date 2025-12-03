from sqlalchemy.orm import Session
from models.produto_model import Produto

# Adicionamos descricao e quantidade nos parâmetros
def criar_produto(db: Session, nome: str, valor: float, descricao: str, quantidade: int):

    # Regra de negócio: Verificar duplicidade
    produto_existente = db.query(Produto).filter(Produto.nome == nome).first()

    if produto_existente:
        # Tratamento de Exceção exigido no PDF
        raise ValueError("Produto já cadastrado no estoque!")

    # Criar produto com os novos campos
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

def listar_produtos(db: Session):
    return db.query(Produto).all()
