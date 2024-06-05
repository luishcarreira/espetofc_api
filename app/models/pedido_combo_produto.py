from app.db.base_class import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class PedidoComboProduto(Base):
    __tablename__ = "pedido_combo_produtos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pedido_combo_id: Mapped[int] = mapped_column(ForeignKey("pedido_combos.id"))
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"))

    pedido_combo: Mapped["PedidoCombo"] = relationship("PedidoCombo", back_populates="produtos_selecionados")
    produto: Mapped["Produto"] = relationship("Produto")
