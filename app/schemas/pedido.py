from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.schemas.item import Item, ItemCreate
from app.schemas.usuario import Usuario

class PedidoBase(BaseModel):
    mesa: int
    status: str

class PedidoCreate(PedidoBase):
    items: List[ItemCreate]

class PedidoUpdate(PedidoBase):
    items: List[ItemCreate]

class Pedido(PedidoBase):
    id: int
    emissao: datetime
    total: float
    created_usuario_id: int
    created_at: datetime
    updated_usuario_id: int | None
    updated_at: datetime | None
    items: List[Item]

    class Config:
        from_attributes = True