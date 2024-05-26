from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45))
    username: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str]

    created_produtos: Mapped['Produto'] = relationship(back_populates="created_usuario", foreign_keys="[Produto.created_usuario_id]")
    updated_produtos: Mapped['Produto'] = relationship(back_populates="updated_usuario", foreign_keys="[Produto.updated_usuario_id]")
    created_pedidos: Mapped['Pedido'] = relationship(back_populates="created_usuario", foreign_keys="[Pedido.created_usuario_id]")
    updated_pedidos: Mapped['Pedido'] = relationship(back_populates="updated_usuario", foreign_keys="[Pedido.updated_usuario_id]")
