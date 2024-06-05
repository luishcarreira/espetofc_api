from typing import List
from pydantic import BaseModel

from app.schemas.pedido_combo_produto import PedidoComboProduto, PedidoComboProdutoCreate


class PedidoComboBase(BaseModel):
    pedido_id: int
    combo_id: int

class PedidoComboCreate(PedidoComboBase):
    produtos_selecionados: List[PedidoComboProdutoCreate]

class PedidoComboUpdate(PedidoComboBase):
    produtos_selecionados: List[PedidoComboProdutoCreate]

class PedidoCombo(PedidoComboBase):
    id: int
    produtos_selecionados: List[PedidoComboProduto] = []

    class Config:
        from_attributes = True
