from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.schemas import transacao as schemas_transacao
from app.crud import transacao as crud_transacao
from app.db.session import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.post("/transacoes/", response_model=schemas_transacao.Transacao)
def create_transacao(transacao: schemas_transacao.TransacaoCreate, db: Session = Depends(get_db)):
    return crud_transacao.create_transacao(db=db, transacao=transacao)

@router.get("/transacoes/{transacao_id}", response_model=schemas_transacao.Transacao)
def read_transacao(transacao_id: int, db: Session = Depends(get_db)):
    db_transacao = crud_transacao.get_transacao(db, transacao_id=transacao_id)
    if db_transacao is None:
        raise HTTPException(status_code=404, detail="Transacao not found")
    return db_transacao

@router.get("/transacoes/", response_model=List[schemas_transacao.Transacao])
def read_transacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    transacoes = crud_transacao.get_transacoes(db, skip=skip, limit=limit)
    return transacoes

@router.put("/transacoes/{transacao_id}", response_model=schemas_transacao.Transacao)
def update_transacao(transacao_id: int, transacao: schemas_transacao.TransacaoUpdate, db: Session = Depends(get_db)):
    db_transacao = crud_transacao.get_transacao(db, transacao_id=transacao_id)
    if db_transacao is None:
        raise HTTPException(status_code=404, detail="Transacao not found")
    return crud_transacao.update_transacao(db=db, db_transacao=db_transacao, transacao_update=transacao)

@router.delete("/transacoes/{transacao_id}", response_model=bool)
def delete_transacao(transacao_id: int, db: Session = Depends(get_db)):
    db_transacao = crud_transacao.get_transacao(db, transacao_id=transacao_id)
    if db_transacao is None:
        raise HTTPException(status_code=404, detail="Transacao not found")
    return crud_transacao.delete_transacao(db=db, transacao_id=transacao_id)