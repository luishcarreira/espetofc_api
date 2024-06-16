from pydantic import BaseModel

from app.schemas.produto import Produto

class ItemBase(BaseModel):
    produto_id: int
    quantidade: int
    valor_unitario: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    pedido_id: int
    produto: Produto

    class Config:
        from_attributes = True