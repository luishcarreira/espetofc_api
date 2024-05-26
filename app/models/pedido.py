import datetime
from typing import List
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

class Pedido(Base):
    __tablename__ = "pedidos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    mesa: Mapped[int]
    data: Mapped[datetime.datetime] = mapped_column()
    status: Mapped[str] = mapped_column(String(20))
    total: Mapped[float]

    items: Mapped[List["Item"]] = relationship(uselist=True, back_populates="pedidos")

    created_usuario: Mapped['Usuario'] = relationship("Usuario", back_populates="pedidos")
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    updated_usuario: Mapped['Usuario'] = relationship("Usuario", back_populates="pedidos")
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)