from datetime import datetime
from pydantic import BaseModel

from app.schemas.usuario import User

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    estoque: int
    preco: float
    categoria_id: int

class ProdutoCreate(ProdutoBase):
    created_usuario: User
    created_at: datetime

class ProdutoUpdate(ProdutoBase):
    updated_usuario: User
    updated_at: datetime

class Produto(ProdutoBase):
    id: int

    class Config:
        from_attributes = True
