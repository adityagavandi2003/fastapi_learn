"""post table

Revision ID: a9f615859367
Revises: c36480c90473
Create Date: 2025-06-11 16:31:32.657543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9f615859367'
down_revision: Union[str, None] = 'c36480c90473'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "post",
        sa.Column("id",sa.INTEGER,primary_key=True),
        sa.Column("caption",sa.String(50),nullable=True),
    )


def downgrade() -> None:
    op.drop_table("post")
