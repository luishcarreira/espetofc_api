from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.pedido_combo import PedidoCombo, PedidoComboCreate, PedidoComboUpdate
from app.crud.pedido_combo import (
    get_pedido_combo,
    get_pedido_combos,
    create_pedido_combo,
    update_pedido_combo,
    delete_pedido_combo,
)
from app.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[PedidoCombo])
def read_pedido_combos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pedido_combos = get_pedido_combos(db, skip=skip, limit=limit)
    return pedido_combos

@router.get("/{pedido_combo_id}", response_model=PedidoCombo)
def read_pedido_combo(pedido_combo_id: int, db: Session = Depends(get_db)):
    pedido_combo = get_pedido_combo(db, pedido_combo_id=pedido_combo_id)
    if pedido_combo is None:
        raise HTTPException(status_code=404, detail="PedidoCombo não encontrado")
    return pedido_combo

@router.post("/", response_model=PedidoCombo)
def create_pedido_combo_endpoint(pedido_combo: PedidoComboCreate, db: Session = Depends(get_db)):
    return create_pedido_combo(db=db, pedido_combo=pedido_combo)

@router.put("/{pedido_combo_id}", response_model=PedidoCombo)
def update_pedido_combo_endpoint(pedido_combo_id: int, pedido_combo: PedidoComboUpdate, db: Session = Depends(get_db)):
    db_pedido_combo = get_pedido_combo(db, pedido_combo_id=pedido_combo_id)
    if db_pedido_combo is None:
        raise HTTPException(status_code=404, detail="PedidoCombo não encontrado")
    return update_pedido_combo(db=db, db_pedido_combo=db_pedido_combo, pedido_combo_update=pedido_combo)

@router.delete("/{pedido_combo_id}", response_model=bool)
def delete_pedido_combo_endpoint(pedido_combo_id: int, db: Session = Depends(get_db)):
    db_pedido_combo = get_pedido_combo(db, pedido_combo_id=pedido_combo_id)
    if db_pedido_combo is None:
        raise HTTPException(status_code=404, detail="PedidoCombo não encontrado")
    return delete_pedido_combo(db=db, pedido_combo_id=pedido_combo_id)
