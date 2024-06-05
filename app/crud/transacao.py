from sqlalchemy.orm import Session
from app.models.transacao import Transacao
from app.schemas.transacao import TransacaoCreate, TransacaoUpdate

def get_transacao(db: Session, transacao_id: int):
    return db.query(Transacao).filter(Transacao.id == transacao_id).first()

def get_transacoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Transacao).offset(skip).limit(limit).all()

def create_transacao(db: Session, transacao: TransacaoCreate):
    db_transacao = Transacao(
        data_transacao=transacao.data_transacao,
        valor=transacao.valor,
        tipo_transacao=transacao.tipo_transacao,
        tipo_pagamento=transacao.tipo_pagamento,
        descricao=transacao.descricao,
        caixa_id=transacao.caixa_id
    )
    db.add(db_transacao)
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

def update_transacao(db: Session, db_transacao: Transacao, transacao_update: TransacaoUpdate):
    db_transacao.data_transacao = transacao_update.data_transacao
    db_transacao.valor = transacao_update.valor
    db_transacao.tipo_transacao = transacao_update.tipo_transacao
    db_transacao.tipo_pagamento = transacao_update.tipo_pagamento
    db_transacao.descricao = transacao_update.descricao
    db_transacao.caixa_id = transacao_update.caixa_id
    db_transacao.pedido_id = transacao_update.pedido_id
    db.commit()
    db.refresh(db_transacao)
    return db_transacao

def delete_transacao(db: Session, transacao_id: int):
    db_transacao = db.query(Transacao).filter(Transacao.id == transacao_id).first()
    db.delete(db_transacao)
    db.commit()
    return True
