"""add mapper to usuarios table #4

Revision ID: a28ec6b0f236
Revises: 7af4ada85645
Create Date: 2024-05-26 21:16:36.241044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a28ec6b0f236'
down_revision: Union[str, None] = '7af4ada85645'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
