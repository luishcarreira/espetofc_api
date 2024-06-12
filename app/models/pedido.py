import datetime
from typing import List
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base
from app.models.pedido_combo import PedidoCombo
from app.models.transacao import Transacao

class Pedido(Base):
    __tablename__ = "pedidos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mesa: Mapped[int]
    emissao: Mapped[datetime.datetime]
    status: Mapped[str] = mapped_column(String(20))
    total: Mapped[float] = mapped_column(nullable=True)
    observacao: Mapped[str] = mapped_column(String(250), nullable=True)

    items: Mapped[List["Item"]] = relationship(back_populates="pedido_items")
    combos: Mapped[List["PedidoCombo"]] = relationship("PedidoCombo", back_populates="pedido")

    created_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    created_usuario: Mapped["Usuario"] = relationship(back_populates="created_pedidos", foreign_keys=[created_usuario_id])
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    updated_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=True)
    updated_usuario: Mapped['Usuario'] = relationship(back_populates="updated_pedidos", foreign_keys=[updated_usuario_id])
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)

    transacoes: Mapped[List["Transacao"]] = relationship("Transacao", back_populates="pedido_transacao")