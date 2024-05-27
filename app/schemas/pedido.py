from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.schemas.item import Item, ItemCreate
from app.schemas.usuario import Usuario

class PedidoBase(BaseModel):
    usuario_id: int
    mesa: int
    emissao: datetime 
    status: str
    total: float
    created_usuario_id: int
    created_at: datetime
    updated_usuario_id: int | None
    updated_at: datetime | None

class PedidoCreate(PedidoBase):
    items: List[ItemCreate]

class PedidoUpdate(PedidoBase):
    items: List[ItemCreate]

class Pedido(PedidoBase):
    id: int
    items: List[Item]

    class Config:
        from_attributes = True