from pydantic import BaseModel


class ComboProdutoBase(BaseModel):
    produto_id: int

class ComboProdutoCreate(ComboProdutoBase):
    pass

class ComboProduto(ComboProdutoBase):
    combo_id: int

    class Config:
        from_attributes = True
