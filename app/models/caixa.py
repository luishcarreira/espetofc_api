
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base


class Caixa(Base):
    __tablename__ = "caixas"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_abertura: Mapped[datetime.datetime]
    data_fechamento: Mapped[datetime.datetime] = mapped_column(nullable=True)
    saldo_inicial: Mapped[float]
    saldo_final: Mapped[float] = mapped_column(nullable=True)

    transacoes: Mapped[list['Transacao']] = relationship(back_populates="caixa")