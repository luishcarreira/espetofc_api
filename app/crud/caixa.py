from datetime import datetime
from sqlalchemy.orm import Session
from app.models.caixa import Caixa
from app.schemas.caixa import CaixaCreate, CaixaUpdate

def get_caixa(db: Session, caixa_id: int):
    return db.query(Caixa).filter(Caixa.id == caixa_id).first()

def get_caixas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Caixa).offset(skip).limit(limit).all()

def create_caixa(db: Session, caixa: CaixaCreate):
    db_caixa = Caixa(
        data_abertura=datetime.now(),
        saldo_inicial=caixa.saldo_inicial
    )
    db.add(db_caixa)
    db.commit()
    db.refresh(db_caixa)
    return db_caixa

def update_caixa(db: Session, db_caixa: Caixa, caixa_update: CaixaUpdate):
    db_caixa.data_fechamento = datetime.now()
    db_caixa.saldo_final = caixa_update.saldo_final
    db.commit()
    db.refresh(db_caixa)
    return db_caixa

def delete_caixa(db: Session, caixa_id: int):
    db_caixa = db.query(Caixa).filter(Caixa.id == caixa_id).first()
    db.delete(db_caixa)
    db.commit()
    return True
