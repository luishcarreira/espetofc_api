"""specify foreign keys for produtos and pedidos

Revision ID: 9ac08acd698f
Revises: 8e895763969f
Create Date: 2024-05-26 20:53:46.793580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ac08acd698f'
down_revision: Union[str, None] = '8e895763969f'
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