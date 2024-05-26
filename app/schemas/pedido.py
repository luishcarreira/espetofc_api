from datetime import datetime
from typing import List
from pydantic import BaseModel

from app.schemas.item import Item, ItemCreate
from app.schemas.usuario import Usuario

class PedidoBase(BaseModel):
    usuario_id: int
    mesa: int
    data: datetime 
    status: str
    total: float

class PedidoCreate(PedidoBase):
    created_usuario: Usuario
    created_at: datetime
    items: List[ItemCreate]

class PedidoUpdate(PedidoBase):
    updated_usuario: Usuario
    updated_at: datetime
    items: List[ItemCreate]

class Pedido(PedidoBase):
    id: int
    
    updated_at: datetime
    items: List[Item]

    class Config:
        orm_mode = True