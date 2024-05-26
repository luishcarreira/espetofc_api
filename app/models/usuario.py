from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base_class import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(String(45))
    username: Mapped[str] = mapped_column(String(50))
    hashed_password: Mapped[str]
