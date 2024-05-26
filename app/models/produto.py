import datetime
from typing import List
from sqlalchemy import ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

class Produto(Base):
    __tablename__ = "produtos"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45))
    descricao: Mapped[str] = mapped_column(String(200))
    preco: Mapped[float]
    estoque: Mapped[int]
    foto_url: Mapped[str] = mapped_column(String(500))

    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped['Categoria'] = relationship(back_populates="produtos")

    created_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    created_usuario: Mapped["Usuario"] = relationship(back_populates="created_produtos", foreign_keys=[created_usuario_id])
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    updated_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    updated_usuario: Mapped['Usuario'] = relationship(back_populates="updated_produtos", foreign_keys=[updated_usuario_id])
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    items: Mapped[List["Item"]] = relationship(back_populates="produto")
