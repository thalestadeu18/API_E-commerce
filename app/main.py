from fastapi import FastAPI
from fastapi.responses import RedirectResponse  # <--- 1. Importe isto
from controllers import usuario_controller
from database import Base, engine

# Cria as tabelas no banco automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Usuários - Projeto POO")

# Inclui as rotas do controller
app.include_router(usuario_controller.router)

# --- ADICIONE ESTA PARTE NO FINAL ---
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")