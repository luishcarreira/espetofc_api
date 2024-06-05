from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from app.schemas.transacao import Transacao


class CaixaBase(BaseModel):
    data_abertura: datetime
    data_fechamento: Optional[datetime]
    saldo_inicial: float
    saldo_final: Optional[float]

class CaixaCreate(CaixaBase):
    pass

class CaixaUpdate(CaixaBase):
    pass

class Caixa(CaixaBase):
    id: int
    transacoes: List[Transacao] = []

    class Config:
        orm_mode = True