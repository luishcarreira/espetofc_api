from fastapi import Depends, FastAPI
from app.api.deps import get_current_user
from app.api.endpoints import categoria, auth, produto, pedido, combo, caixa, transacao, pedido_combo

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])

app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"], dependencies=[Depends(get_current_user)])
app.include_router(produto.router, prefix="/produtos", tags=["Produtos"], dependencies=[Depends(get_current_user)])
app.include_router(pedido.router, prefix="/pedidos", tags=["Pedidos"], dependencies=[Depends(get_current_user)])
app.include_router(combo.router, prefix="/combos", tags=["Combos"], dependencies=[Depends(get_current_user)])
app.include_router(pedido_combo.router, prefix="/pedidoscombo", tags=["Pedidos Combo"], dependencies=[Depends(get_current_user)])
app.include_router(caixa.router, prefix="/caixas", tags=["Caixas"], dependencies=[Depends(get_current_user)])
app.include_router(transacao.router, prefix="/transacoes", tags=["Transações"], dependencies=[Depends(get_current_user)])

@app.get("/health")
def health_check():
    return {"status": "API is working🔥"}
