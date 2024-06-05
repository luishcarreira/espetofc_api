from typing import List
from app.db.base_class import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.combo import Combo
from app.models.pedido_combo_produto import PedidoComboProduto

class PedidoCombo(Base):
    __tablename__ = "pedido_combos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"))
    combo_id: Mapped[int] = mapped_column(ForeignKey("combos.id"))

    pedido: Mapped["Pedido"] = relationship("Pedido", back_populates="combos")
    combo: Mapped["Combo"] = relationship("Combo")
    produtos_selecionados: Mapped[List["PedidoComboProduto"]] = relationship("PedidoComboProduto", back_populates="pedido_combo")
