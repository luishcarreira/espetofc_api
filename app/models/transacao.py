import datetime
from typing import Literal
from sqlalchemy import ForeignKey, String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base

TipoTransacaoEnum = Literal["Entrada", "Saída"]
TipoPagamentoEnum = Literal["Dinheiro","CartaoCredito","CartaoDebito","Pix","TransferenciaBancaria","Outros"]

class Transacao(Base):
    __tablename__ = "transacoes"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    data_transacao: Mapped[datetime.datetime]
    valor: Mapped[float]
    tipo_transacao: Mapped[TipoTransacaoEnum] = mapped_column(Enum("Entrada", "Saída", name="tipo_transacao_enum"))
    tipo_pagamento: Mapped[TipoPagamentoEnum] = mapped_column(Enum("Dinheiro", "CartaoCredito", "CartaoDebito", "Pix", "TransferenciaBancaria", "Outros",  name="tipo_pagamento_enum"))
    descricao: Mapped[str] = mapped_column(String(200))

    caixa_id: Mapped[int] = mapped_column(ForeignKey("caixas.id"))
    caixa: Mapped['Caixa'] = relationship(back_populates="transacoes")

    pedido_id: Mapped[int] = mapped_column(ForeignKey("pedidos.id"))
    pedido: Mapped['Pedido'] = relationship(back_populates="transacoes")