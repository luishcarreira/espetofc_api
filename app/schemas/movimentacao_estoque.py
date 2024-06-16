from pydantic import BaseModel
from datetime import datetime

from app.schemas.usuario import Usuario

class MovimentacaoEstoqueBase(BaseModel):
    produto_id: int
    quantidade: int
    tipo_movimentacao: str  # "Entrada" ou "Saída"
    data_movimentacao: datetime
    observacao: str

class MovimentacaoEstoqueCreate(MovimentacaoEstoqueBase):
    usuario_id: int

class MovimentacaoEstoque(MovimentacaoEstoqueBase):
    id: int
    usuario: Usuario 

    class Config:
        from_attributes = True
