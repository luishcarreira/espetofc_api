from typing import List
from app.db.base_class import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class ComboProduto(Base):
    __tablename__ = "combo_produtos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    combo_id: Mapped[int] = mapped_column(ForeignKey("combos.id"))
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"))

    combo: Mapped["Combo"] = relationship("Combo", back_populates="produtos")
    produto: Mapped["Produto"] = relationship("Produto")
