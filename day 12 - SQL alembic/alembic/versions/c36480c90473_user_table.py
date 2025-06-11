"""user table

Revision ID: c36480c90473
Revises: 
Create Date: 2025-06-11 16:26:31.876866

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c36480c90473'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
    "users",
    sa.Column("id", sa.INTEGER, primary_key=True),
    sa.Column("name", sa.String(50), nullable=False),
    sa.Column("email", sa.String, nullable=False),
)


def downgrade() -> None:
    op.drop_table('users')

