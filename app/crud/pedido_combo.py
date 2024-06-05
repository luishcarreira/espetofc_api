from sqlalchemy.orm import Session
from app.models.pedido_combo import PedidoCombo
from app.models.pedido_combo_produto import PedidoComboProduto
from app.schemas.pedido_combo import PedidoComboCreate, PedidoComboUpdate

def get_pedido_combo(db: Session, pedido_combo_id: int):
    return db.query(PedidoCombo).filter(PedidoCombo.id == pedido_combo_id).first()

def get_pedido_combos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(PedidoCombo).offset(skip).limit(limit).all()

def create_pedido_combo(db: Session, pedido_combo: PedidoComboCreate):
    db_pedido_combo = PedidoCombo(
        pedido_id=pedido_combo.pedido_id,
        combo_id=pedido_combo.combo_id
    )
    db.add(db_pedido_combo)
    db.commit()
    db.refresh(db_pedido_combo)

    for produto in pedido_combo.produtos_selecionados:
        db_pedido_combo_produto = PedidoComboProduto(
            pedido_combo_id=db_pedido_combo.id,
            produto_id=produto.produto_id
        )
        db.add(db_pedido_combo_produto)
    db.commit()
    
    db.refresh(db_pedido_combo)
    return db_pedido_combo

def update_pedido_combo(db: Session, db_pedido_combo: PedidoCombo, pedido_combo_update: PedidoComboUpdate):
    db_pedido_combo.pedido_id = pedido_combo_update.pedido_id
    db_pedido_combo.combo_id = pedido_combo_update.combo_id
    db.commit()

    # Atualizar produtos do pedido combo
    db.query(PedidoComboProduto).filter(PedidoComboProduto.pedido_combo_id == db_pedido_combo.id).delete()
    for produto in pedido_combo_update.produtos_selecionados:
        db_pedido_combo_produto = PedidoComboProduto(
            pedido_combo_id=db_pedido_combo.id,
            produto_id=produto.produto_id
        )
        db.add(db_pedido_combo_produto)
    db.commit()
    
    db.refresh(db_pedido_combo)
    return db_pedido_combo

def delete_pedido_combo(db: Session, pedido_combo_id: int):
    db_pedido_combo = db.query(PedidoCombo).filter(PedidoCombo.id == pedido_combo_id).first()
    db.query(PedidoComboProduto).filter(PedidoComboProduto.pedido_combo_id == pedido_combo_id).delete()
    db.delete(db_pedido_combo)
    db.commit()
    return True
