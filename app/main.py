from fastapi import FastAPI
from controllers import usuario_controller
from database import Base, engine

# Cria as tabelas no banco automaticamente
Base.metadata.create_all(bind=engine)
app = FastAPI(title="API de Usuários - Projeto POO")
# Inclui as rotas do controller
app.include_router(usuario_controller.router)
