from app.db.base_class import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Item(Base):
    __tablename__ = "items"
    
    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"), primary_key=True)
    produto_id: Mapped[int] = mapped_column(ForeignKey("produtos.id"), primary_key=True)
    
    quantidade: Mapped[int]
    valor: Mapped[float]
    
    pedido: Mapped['Pedido'] = relationship("Pedido", back_populates="items")
    produto: Mapped['Produto'] = relationship("Produto", back_populates="items")