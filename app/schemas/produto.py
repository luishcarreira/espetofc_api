from datetime import datetime
from pydantic import BaseModel

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
    created_usuario_id: int
    created_at: datetime
    updated_usuario_id: int
    updated_at: datetime

    class Config:
        from_attributes = True
