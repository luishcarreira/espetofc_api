from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import caixa as schemas_caixa
from app.crud import caixa as crud_caixa
from app.db.session import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/", response_model=schemas_caixa.Caixa)
def create_caixa(caixa: schemas_caixa.CaixaCreate, db: Session = Depends(get_db)):
    return crud_caixa.create_caixa(db=db, caixa=caixa)

@router.get("/{caixa_id}", response_model=schemas_caixa.Caixa)
def read_caixa(caixa_id: int, db: Session = Depends(get_db)):
    db_caixa = crud_caixa.get_caixa(db, caixa_id=caixa_id)
    if db_caixa is None:
        raise HTTPException(status_code=404, detail="Caixa not found")
    return db_caixa

@router.get("/", response_model=List[schemas_caixa.Caixa])
def read_caixas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    caixas = crud_caixa.get_caixas(db, skip=skip, limit=limit)
    return caixas

@router.put("/{caixa_id}", response_model=schemas_caixa.Caixa)
def update_caixa(caixa_id: int, caixa: schemas_caixa.CaixaUpdate, db: Session = Depends(get_db)):
    db_caixa = crud_caixa.get_caixa(db, caixa_id=caixa_id)
    if db_caixa is None:
        raise HTTPException(status_code=404, detail="Caixa not found")
    return crud_caixa.update_caixa(db=db, db_caixa=db_caixa, caixa_update=caixa)

@router.delete("/{caixa_id}", response_model=bool)
def delete_caixa(caixa_id: int, db: Session = Depends(get_db)):
    db_caixa = crud_caixa.get_caixa(db, caixa_id=caixa_id)
    if db_caixa is None:
        raise HTTPException(status_code=404, detail="Caixa not found")
    return crud_caixa.delete_caixa(db=db, caixa_id=caixa_id)