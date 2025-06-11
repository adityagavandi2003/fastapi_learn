"""add uniques contraint to email

Revision ID: 12848f5b6bab
Revises: cdc736eec980
Create Date: 2025-06-11 17:13:55.912338

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12848f5b6bab'
down_revision: Union[str, None] = 'cdc736eec980'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.create_unique_constraint("uq_users_email",['email'])

def downgrade() -> None:
    with op.batch_alter_table("users") as batch:
        batch.drop_constraint("uq_users_email",type_="unique")
