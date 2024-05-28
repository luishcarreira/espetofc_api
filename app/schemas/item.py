from pydantic import BaseModel

class ItemBase(BaseModel):
    produto_id: int
    quantidade: int
    valor: float

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    pedido_id: int

    class Config:
        from_attributes = True