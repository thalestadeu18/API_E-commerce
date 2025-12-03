from fastapi import FastAPI
from database import Base, engine
from controllers import produto_controller

# cria as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Produtos")

# importa as rotas
app.include_router(produto_controller.router)
