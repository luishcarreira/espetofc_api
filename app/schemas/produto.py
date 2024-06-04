from datetime import datetime
from pydantic import BaseModel

from app.schemas.categoria import Categoria

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    estoque: int
    preco: float
    categoria_id: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int
    categoria: Categoria
    created_usuario_id: int
    created_at: datetime
    updated_usuario_id: int | None
    updated_at: datetime | None

    class Config:
        from_attributes = True
