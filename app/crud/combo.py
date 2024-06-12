from sqlalchemy.orm import Session
from app.models.combo import Combo
from app.models.combo_produto import ComboProduto
from app.schemas.combo import ComboCreate, ComboUpdate

def get_combo(db: Session, combo_id: int):
    return db.query(Combo).filter(Combo.id == combo_id).first()

def get_combo_produto(db: Session, combo_id: int, combo_produto_id: int):
    return db.query(ComboProduto).filter(ComboProduto.combo_id == combo_id, ComboProduto.produto_id == combo_produto_id).first()

def get_combos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Combo).offset(skip).limit(limit).all()

def create_combo(db: Session, combo: ComboCreate):
    db_combo = Combo(
        nome=combo.nome,
        preco=combo.preco,
        quantidade_espeto=combo.quantidade_espeto
    )
    db.add(db_combo)
    db.commit()
    db.refresh(db_combo)

    for produto in combo.produtos:
        db_combo_produto = ComboProduto(
            combo_id=db_combo.id,
            produto_id=produto.produto_id
        )
        db.add(db_combo_produto)
    db.commit()
    
    db.refresh(db_combo)
    return db_combo

def update_combo(db: Session, db_combo: Combo, combo_update: ComboUpdate):
    db_combo.nome = combo_update.nome
    db_combo.preco = combo_update.preco
    db_combo.quantidade_espeto = combo_update.quantidade_espeto
    db.commit()

    # Atualizar produtos do combo
    db.query(ComboProduto).filter(ComboProduto.combo_id == db_combo.id).delete()
    for produto in combo_update.produtos:
        db_combo_produto = ComboProduto(
            combo_id=db_combo.id,
            produto_id=produto.produto_id
        )
        db.add(db_combo_produto)
    db.commit()
    
    db.refresh(db_combo)
    return db_combo

def delete_combo(db: Session, combo_id: int):
    db_combo = db.query(Combo).filter(Combo.id == combo_id).first()
    db.query(ComboProduto).filter(ComboProduto.combo_id == combo_id).delete()
    db.delete(db_combo)
    db.commit()
    return True

def delete_combo_produto(db: Session, combo_id: int, combo_produto_id: int):
    db_combo = db.query(ComboProduto).filter(ComboProduto.combo_id == combo_id, ComboProduto.produto_id == combo_produto_id).first()
    db.delete(db_combo)
    db.commit()
    return True
