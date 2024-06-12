from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.schemas.transacao import Transacao


class CaixaBase(BaseModel):
    pass

class CaixaCreate(CaixaBase):
    saldo_inicial: float

class CaixaUpdate(CaixaBase):
    saldo_final: Optional[float]

class Caixa(CaixaBase):
    id: int
    data_abertura: datetime
    saldo_inicial: float
    saldo_final: Optional[float]
    data_fechamento: Optional[datetime]
    transacoes: List[Transacao] = []

    class Config:
        orm_mode = True