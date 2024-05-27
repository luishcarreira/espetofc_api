from pydantic import BaseModel

class CategoriaBase(BaseModel):
    nome: str
    descricao: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        from_attributes = True

