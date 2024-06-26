"""change field for item pedido to valor_unitario

Revision ID: eec23b11767f
Revises: 1a53fdc9de2f
Create Date: 2024-06-14 02:35:19.713496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eec23b11767f'
down_revision: Union[str, None] = '1a53fdc9de2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('valor_unitario', sa.Float(), nullable=False))
    op.drop_column('items', 'valor')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('valor', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_column('items', 'valor_unitario')
    # ### end Alembic commands ###
