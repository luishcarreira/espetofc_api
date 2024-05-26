import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base_class import Base


class Categoria(Base):
    __tablename__ = "categorias"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45))
    descricao: Mapped[str] = mapped_column(String(200))

    created_usr: Mapped[str] = mapped_column()
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime)

    produtos: Mapped["Produto"] = relationship(back_populates="categoria")