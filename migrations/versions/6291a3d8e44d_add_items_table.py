"""add items table

Revision ID: 6291a3d8e44d
Revises: 3004064964cb
Create Date: 2024-05-23 20:33:24.585785

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6291a3d8e44d'
down_revision: Union[str, None] = '3004064964cb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mesa', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=200), nullable=False),
    sa.Column('status', sa.String(length=200), nullable=False),
    sa.Column('total', sa.Float(), nullable=False),
    sa.Column('created_usr', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('pedido_id', sa.Integer(), nullable=False),
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('valor', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedidos.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['produtos.id'], ),
    sa.PrimaryKeyConstraint('pedido_id', 'produto_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('pedidos')
    # ### end Alembic commands ###
