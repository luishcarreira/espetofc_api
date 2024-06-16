from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.schemas.categoria import Categoria
from app.schemas.movimentacao_estoque import MovimentacaoEstoque

class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    estoque_minimo: int
    estoque_atual: int
    preco_custo: float
    preco_venda: float
    medida: str
    categoria_id: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int
    categoria: Categoria
    movimentacoes_estoque: List[MovimentacaoEstoque]
    created_usuario_id: int
    created_at: datetime
    updated_usuario_id: int | None
    updated_at: datetime | None

    class Config:
        from_attributes = True
