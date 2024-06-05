from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransacaoBase(BaseModel):
    data_transacao: datetime
    valor: float
    tipo_transacao: str
    tipo_pagamento: str 
    descricao: str

class TransacaoCreate(TransacaoBase):
    caixa_id: int

class TransacaoUpdate(TransacaoBase):
    caixa_id: Optional[int] = None
    pedido_id: Optional[int] = None

class Transacao(TransacaoBase):
    id: int
    caixa_id: int
    pedido_id: Optional[int] = None

    class Config:
        orm_mode = True