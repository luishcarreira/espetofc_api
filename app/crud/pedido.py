from sqlalchemy.orm import Session
from app.models.pedido import Pedido, Item
from app.schemas.pedido import PedidoCreate, PedidoUpdate

def get_pedido(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pedido).offset(skip).limit(limit).all()

def create_pedido(db: Session, pedido: PedidoCreate):
    db_pedido = Pedido(usuario_id=pedido.usuario_id, total=pedido.total)
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    
    for item in pedido.items:
        db_item = Item(pedido_id=db_pedido.id, produto_id=item.produto_id, quantidade=item.quantidade)
        db.add(db_item)
    
    db.commit()
    return db_pedido

def update_pedido(db: Session, db_pedido: Pedido, pedido_update: PedidoUpdate):
    db_pedido.usuario_id = pedido_update.usuario_id
    db_pedido.total = pedido_update.total
    db.commit()
    db.refresh(db_pedido)
    
    db.query(Item).filter(Item.pedido_id == db_pedido.id).delete()
    db.commit()
    
    for item in pedido_update.items:
        db_item = Item(pedido_id=db_pedido.id, produto_id=item.produto_id, quantidade=item.quantidade)
        db.add(db_item)
    
    db.commit()
    return db_pedido

def delete_pedido(db: Session, db_pedido: Pedido):
    db.query(Item).filter(Item.pedido_id == db_pedido.id).delete()
    db.commit()
    db.delete(db_pedido)
    db.commit()
    return db_pedido
