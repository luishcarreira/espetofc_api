from typing import List
from app.db.base_class import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.combo_produto import ComboProduto


class Combo(Base):
    __tablename__ = "combos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45))
    preco: Mapped[float]
    quantidade_espeto: Mapped[int]
    produtos: Mapped[List["ComboProduto"]] = relationship("ComboProduto", back_populates="combo")
