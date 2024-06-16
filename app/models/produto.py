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
    preco_custo: Mapped[float]
    preco_venda: Mapped[float]
    medida: Mapped[str] = mapped_column(String(2))
    estoque_minimo: Mapped[int]
    estoque_atual: Mapped[int]
    foto_url: Mapped[str] = mapped_column(String(500), nullable=True)

    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))
    categoria: Mapped['Categoria'] = relationship(back_populates="produtos")

    created_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    created_usuario: Mapped["Usuario"] = relationship(back_populates="created_produtos", foreign_keys=[created_usuario_id])
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    updated_usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), nullable=True)
    updated_usuario: Mapped['Usuario'] = relationship(back_populates="updated_produtos", foreign_keys=[updated_usuario_id])
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)

    items: Mapped[List["Item"]] = relationship(back_populates="produto")

    movimentacoes_estoque: Mapped[List["MovimentacaoEstoque"]] = relationship(back_populates="produto")
