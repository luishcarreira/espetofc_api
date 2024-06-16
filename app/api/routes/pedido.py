from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.pedido import Pedido, PedidoCreate, PedidoUpdate
from app.crud.pedido import (
    get_pedido,
    get_pedidos,
    create_pedido,
    update_pedido,
    delete_pedido,
)
from app.crud.item import (
    get_item,
    get_items_pedido,
    delete_item,
)

from app.api.deps import get_db, get_current_user
from app.models.usuario import Usuario

router = APIRouter()

@router.get("/", response_model=List[Pedido])
def read_pedidos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pedidos = get_pedidos(db, skip=skip, limit=limit)
    return pedidos

@router.get("/{pedido_id}", response_model=Pedido)
def read_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = get_pedido(db, pedido_id=pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

@router.post("/", response_model=Pedido)
def create_pedido_endpoint(pedido: PedidoCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return create_pedido(db=db, pedido=pedido, current_user=current_user)

@router.put("/{pedido_id}", response_model=Pedido)
def update_pedido_endpoint(pedido_id: int, pedido: PedidoUpdate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    db_pedido = get_pedido(db, pedido_id=pedido_id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return update_pedido(db=db, db_pedido=db_pedido, pedido_update=pedido, current_user=current_user)

@router.delete("/{pedido_id}", response_model=bool)
def delete_pedido_endpoint(pedido_id: int, db: Session = Depends(get_db)):
    db_pedido = get_pedido(db, pedido_id=pedido_id)
    if db_pedido is None:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return delete_pedido(db=db, db_pedido=db_pedido)

# itens 
@router.delete("/{pedido_id}/produto/{produto_id}", response_model=bool)
def delete_item_pedido_endpoint(pedido_id: int, produto_id: int, db: Session = Depends(get_db)):
    db_item = get_item(db, pedido_id=pedido_id, produto_id=produto_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return delete_item(db=db, pedido_id=db_item.pedido_id, produto_id=db_item.produto_id)
