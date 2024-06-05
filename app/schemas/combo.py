from typing import List
from pydantic import BaseModel

from app.schemas.combo_produto import ComboProdutoCreate, ComboProduto


class ComboBase(BaseModel):
    nome: str
    preco: float

class ComboCreate(ComboBase):
    produtos: List[ComboProdutoCreate]

class ComboUpdate(ComboBase):
    produtos: List[ComboProdutoCreate]

class Combo(ComboBase):
    id: int
    produtos: List[ComboProduto] = []

    class Config:
        from_attributes = True
