from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    username: str

class UsuarioCreate(UsuarioBase):
    password: str

class Usuario(UsuarioBase):
    id: int

    class Config:
        from_attributes = True
