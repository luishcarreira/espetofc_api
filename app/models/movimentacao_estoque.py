from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class MovimentacaoEstoque(Base):
    __tablename__ = "movimentacoes_estoque"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"))
    produto: Mapped['Produto'] = relationship(back_populates="movimentacoes_estoque")
    quantidade: Mapped[int]
    tipo_movimentacao: Mapped[str] = mapped_column(String(20))  # Entrada ou Saída
    data_movimentacao: Mapped[datetime] = mapped_column(DateTime)
    observacao: Mapped[str] = mapped_column(String(200))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    usuario: Mapped['Usuario'] = relationship(back_populates="movimentacoes_estoque")
