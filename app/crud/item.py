from sqlalchemy.orm import Session
from app.models.item import Item

def get_item(db: Session, pedido_id: int, produto_id: int):
    return db.query(Item).filter(Item.pedido_id == pedido_id, Item.produto_id == produto_id).first()

def get_items_pedido(db: Session, pedido_id: int):
    return db.query(Item).filter(Item.pedido_id == pedido_id).all()

def delete_item(db: Session, pedido_id: int, produto_id: int):
    db.query(Item).filter(Item.pedido_id == pedido_id, Item.produto_id == produto_id).delete()
    db.commit()
    return True
