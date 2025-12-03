from fastapi import FastAPI
from database import Base, engine
from fastapi.responses import RedirectResponse
from controllers import produto_controller
from controllers import usuario_controller 

# Cria tabelas (produtos e usuarios)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API E-commerce (AV2)")

# Rotas de Produtos (Obrigatório para o tema)
app.include_router(produto_controller.router)

# Rotas de Usuários (Opcional, mas enriquece o projeto como 'Clientes')
app.include_router(usuario_controller.router)

@app.get("/", include_in_schema=False) # include_in_schema=False esconde essa rota da doc
def root():
    return RedirectResponse(url="/docs")