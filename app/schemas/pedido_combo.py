from typing import List
from pydantic import BaseModel

from app.schemas.pedido_combo_produto import PedidoComboProduto, PedidoComboProdutoCreate


class PedidoComboBase(BaseModel):
    pedido_id: int
    combo_id: int

class PedidoComboCreate(PedidoComboBase):
    espetos_selecionados: List[PedidoComboProdutoCreate]

class PedidoComboUpdate(PedidoComboBase):
    espetos_selecionados: List[PedidoComboProdutoCreate]

class PedidoCombo(PedidoComboBase):
    id: int
    espetos_selecionados: List[PedidoComboProduto] = []

    class Config:
        from_attributes = True
