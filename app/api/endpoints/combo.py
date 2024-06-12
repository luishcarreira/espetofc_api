from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.combo import Combo, ComboCreate, ComboUpdate
from app.crud.combo import (
    get_combo,
    get_combo_produto,
    get_combos,
    create_combo,
    update_combo,
    delete_combo,
    delete_combo_produto,
)
from app.api.deps import get_db

router = APIRouter()

@router.get("/", response_model=List[Combo])
def read_combos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    combos = get_combos(db, skip=skip, limit=limit)
    return combos

@router.get("/{combo_id}", response_model=Combo)
def read_combo(combo_id: int, db: Session = Depends(get_db)):
    combo = get_combo(db, combo_id=combo_id)
    if combo is None:
        raise HTTPException(status_code=404, detail="Combo não encontrado")
    return combo

@router.post("/", response_model=Combo)
def create_combo_endpoint(combo: ComboCreate, db: Session = Depends(get_db)):
    return create_combo(db=db, combo=combo)

@router.put("/{combo_id}", response_model=Combo)
def update_combo_endpoint(combo_id: int, combo: ComboUpdate, db: Session = Depends(get_db)):
    db_combo = get_combo(db, combo_id=combo_id)
    if db_combo is None:
        raise HTTPException(status_code=404, detail="Combo não encontrado")
    return update_combo(db=db, db_combo=db_combo, combo_update=combo)

@router.delete("/{combo_id}", response_model=bool)
def delete_combo_endpoint(combo_id: int, db: Session = Depends(get_db)):
    db_combo = get_combo(db, combo_id=combo_id)
    if db_combo is None:
        raise HTTPException(status_code=404, detail="Combo não encontrado")
    return delete_combo(db=db, combo_id=combo_id)

@router.delete("/{combo_id}/{combo_produto_id}", response_model=bool)
def delete_combo_endpoint(combo_id: int, combo_produto_id: int, db: Session = Depends(get_db)):
    db_combo = get_combo_produto(db, combo_id=combo_id, combo_produto_id=combo_produto_id)
    if db_combo is None:
        raise HTTPException(status_code=404, detail="Combo não encontrado")
    return delete_combo_produto(db=db, combo_id=combo_id, combo_produto_id=combo_produto_id)
