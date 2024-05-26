import datetime
from typing import List
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

class Pedido(Base):
    __tablename__ = "pedidos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mesa: Mapped[int]
    emissao: Mapped[datetime.datetime] = mapped_column()
    status: Mapped[str] = mapped_column(String(20))
    total: Mapped[float]

    items: Mapped[List["Item"]] = relationship(back_populates="pedido")

    created_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    created_usuario: Mapped["Usuario"] = relationship(back_populates="created_pedidos", foreign_keys=[created_usuario_id])
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    updated_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    updated_usuario: Mapped['Usuario'] = relationship(back_populates="updated_pedidos", foreign_keys=[updated_usuario_id])
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)