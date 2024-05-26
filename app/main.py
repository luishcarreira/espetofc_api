from fastapi import Depends, FastAPI
from app.api.deps import get_current_user
from app.api.endpoints import categoria, auth, produto, pedido

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

app.include_router(categoria.router, prefix="/categorias", tags=["categorias"], dependencies=[Depends(get_current_user)])
app.include_router(produto.router, prefix="/produtos", tags=["produtos"], dependencies=[Depends(get_current_user)])
app.include_router(pedido.router, prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(get_current_user)])

@app.get("/health")
def health_check():
    return {"status": "API is working🔥"}
