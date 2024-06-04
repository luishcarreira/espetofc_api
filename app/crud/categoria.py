from typing import List
from sqlalchemy.orm import Session
from app.models.categoria import Categoria
from app.schemas.categoria import CategoriaCreate, CategoriaUpdate


def get_categorias(db: Session, skip: int = 0, limit: int = 100) -> List[Categoria]:
    return db.query(Categoria).offset(skip).limit(limit).all()

def get_categoria(db: Session, id: int) -> Categoria:
    return db.query(Categoria).filter(Categoria.id == id).first()

def create_categoria(db: Session, categoria: CategoriaCreate) -> Categoria:
    db_categoria = Categoria(**categoria.model_dump())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, db_categoria: Categoria, categoria_update: CategoriaUpdate) -> Categoria:
    db_categoria.nome = categoria_update.nome
    db_categoria.descricao = categoria_update.descricao
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, db_categoria: Categoria) -> Categoria:
    db.delete(db_categoria)
    db.commit()
    return True