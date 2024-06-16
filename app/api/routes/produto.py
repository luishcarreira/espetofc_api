from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.produto import Produto, ProdutoCreate, ProdutoUpdate
from app.crud.produto import (
    get_produto,
    get_produtos,
    create_produto,
    update_produto,
    delete_produto,
)
from app.api.deps import get_db, get_current_user

router = APIRouter()

@router.get("/", response_model=List[Produto])
def read_produtos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    produtos = get_produtos(db, skip=skip, limit=limit)
    return produtos

@router.get("/{produto_id}", response_model=Produto)
def read_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = get_produto(db, produto_id=produto_id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto

@router.post("/", response_model=Produto)
def create_produto_endpoint(produto: ProdutoCreate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    return create_produto(db=db, produto=produto, current_user=current_user)

@router.put("/{produto_id}", response_model=Produto)
def update_produto_endpoint(produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_db), current_user: Usuario = Depends(get_current_user)):
    db_produto = get_produto(db, produto_id=produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return update_produto(db=db, db_produto=db_produto, produto_update=produto, current_user=current_user)

@router.delete("/{produto_id}", response_model=Produto)
def delete_produto_endpoint(produto_id: int, db: Session = Depends(get_db)):
    db_produto = get_produto(db, produto_id=produto_id)
    if db_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return delete_produto(db=db, db_produto=db_produto)
