from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from services import usuario_service

router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.post("/")
def criar_usuario(nome: str, cpf: str, senha: str, email: str, db: Session = Depends(get_db)):
    try:
        usuario = usuario_service.criar_usuario(db, nome, cpf, senha, email)
        return usuario
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return usuario_service.listar_usuarios(db)
