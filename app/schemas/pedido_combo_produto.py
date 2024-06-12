from pydantic import BaseModel


class PedidoComboProdutoBase(BaseModel):
    produto_id: int

class PedidoComboProdutoCreate(PedidoComboProdutoBase):
    pass

class PedidoComboProduto(PedidoComboProdutoBase):
    id: int
    pedido_combo_id: int

    class Config:
        from_attributes = True
