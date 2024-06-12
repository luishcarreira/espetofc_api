from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import categoria as categoria_schema
from app.crud import categoria as categoria_crud
from app.db.session import get_db

router = APIRouter()

@router.get("/", response_model=List[categoria_schema.Categoria])
def get_categorias(skip: int = 0, limit: int = 100,db: Session = Depends(get_db)):
    categorias = categoria_crud.get_categorias(db, skip=skip, limit=limit)
    return categorias

@router.get("/{categoria_id}", response_model=categoria_schema.Categoria)
def get_categoria(categoria_id:int, db: Session = Depends(get_db)):
    categoria = categoria_crud.get_categoria(db, id=categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.post("/", response_model=categoria_schema.Categoria)
def create_produto(categoria_in: categoria_schema.CategoriaCreate, db: Session = Depends(get_db)):
    categoria = categoria_crud.create_categoria(db, categoria_in)
    return categoria

@router.put("/{categoria_id}", response_model=categoria_schema.Categoria)
def update_categoria_endpoint(categoria_id: int, categoria: categoria_schema.CategoriaUpdate, db: Session = Depends(get_db)):
    db_categoria = categoria_crud.get_categoria(db, id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria_crud.update_categoria(db=db, db_categoria=db_categoria, categoria_update=categoria)

@router.delete("/{categoria_id}", response_model=bool)
def delete_categoria_endpoint(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = categoria_crud.get_categoria(db=db, id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria_crud.delete_categoria(db=db, db_categoria=db_categoria)
