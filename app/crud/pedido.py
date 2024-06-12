from datetime import datetime
from sqlalchemy.orm import Session
from app.models.item import Item
from app.models.pedido import Pedido
from app.schemas.pedido import PedidoCreate, PedidoUpdate
from app.models.usuario import Usuario

def get_pedido(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()

def get_pedidos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Pedido).offset(skip).limit(limit).all()

def create_pedido(db: Session, pedido: PedidoCreate, current_user: Usuario):
    db_pedido = Pedido(
        mesa=pedido.mesa,
        emissao=datetime.now(),
        status=pedido.status,
        observacao=pedido.observacao if pedido.observacao is not None else '',
        created_usuario_id=current_user.id,
        created_at=datetime.now(),
        total=0.0
    )
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    
    valor_total: float = 0.0
    for item in pedido.items:
        valor_total += (item.valor * item.quantidade)
        db_item = Item(pedido_id=db_pedido.id, produto_id=item.produto_id, quantidade=item.quantidade, valor=item.valor)
        db.add(db_item)

    db_pedido.total = valor_total
    db.commit()
    return db_pedido

def update_pedido(db: Session, db_pedido: Pedido, pedido_update: PedidoUpdate, current_user: Usuario):
    db_pedido.mesa=pedido_update.mesa,
    db_pedido.status=pedido_update.status,
    db_pedido.observacao=pedido_update.observacao,
    db_pedido.updated_usuario_id = current_user.id
    db_pedido.updated_at = datetime.now()
    db.commit()
    db.refresh(db_pedido)
    
    db.query(Item).filter(Item.pedido_id == db_pedido.id).delete()
    db.commit()
    
    valor_total: float = 0.0
    for item in pedido_update.items:
        valor_total += (item.valor * item.quantidade)
        db_item = Item(pedido_id=db_pedido.id, produto_id=item.produto_id, quantidade=item.quantidade, valor=item.valor)
        db.add(db_item)

    db_pedido.total = valor_total
    db.commit()
    return db_pedido

def delete_pedido(db: Session, db_pedido: Pedido):
    db.query(Item).filter(Item.pedido_id == db_pedido.id).delete()
    db.commit()
    db.delete(db_pedido)
    db.commit()
    return True
