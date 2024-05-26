from datetime import datetime
from sqlalchemy.orm import Session
from app.models.produto import Produto
from app.schemas.produto import ProdutoCreate, ProdutoUpdate
from app.models.usuario import Usuario

def get_produto(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def get_produtos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Produto).offset(skip).limit(limit).all()

def create_produto(db: Session, produto: ProdutoCreate, current_user: Usuario):
    db_produto = Produto(
        nome=produto.nome,
        preco=produto.preco,
        descricao=produto.descricao,
        categoria_id=produto.categoria_id,
        created_usuario_id=current_user.id,
        created_at=datetime.now()
    )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def update_produto(db: Session, db_produto: Produto, produto_update: ProdutoUpdate, current_user: Usuario):
    db_produto.nome = produto_update.nome
    db_produto.preco = produto_update.preco
    db_produto.descricao = produto_update.descricao
    db_produto.updated_usuario_id = current_user.id
    db_produto.updated_at = datetime.now()
    db.commit()
    db.refresh(db_produto)
    return db_produto

def delete_produto(db: Session, db_produto: Produto):
    db.delete(db_produto)
    db.commit()
    return db_produto
