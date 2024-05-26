import datetime
from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nome: str
    descricao: str
    created_usr: str
    created_at: datetime.datetime

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        from_attributes = True

