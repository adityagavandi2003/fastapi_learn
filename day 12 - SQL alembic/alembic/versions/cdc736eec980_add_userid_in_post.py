"""add userid in post

Revision ID: cdc736eec980
Revises: a9f615859367
Create Date: 2025-06-11 16:56:39.207781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdc736eec980'
down_revision: Union[str, None] = 'a9f615859367'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('post',sa.Column('user_id',sa.Integer()))


def downgrade() -> None:
    op.drop_column("post", "user_id")
