from models.usuario_model import usuario
from sqlalchemy.orm import Session

def criar_usuario(db: Session, nome: str, email: str, cpf: str, senha: str):
    
    
    
    
# Verifica se já existe um usuário com o mesmo email
    usuario_existente = db.query(usuario).filter(usuario.email == email).first()

    if usuario_existente:
        raise ValueError("Email já cadastrado!")
    
# Cria o novo usuário
    novo_usuario = usuario(nome=nome, email=email, CPF=cpf, senha=senha)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario
def listar_usuarios(db: Session):
    
    
    
    
    return db.query(usuario).all()
