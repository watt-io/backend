"""create filmes table

Revision ID: 001
Revises:
Create Date: 2026-05-16

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "filmes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("titulo", sa.String(length=255), nullable=False),
        sa.Column("diretor", sa.String(length=255), nullable=False),
        sa.Column("ano", sa.Integer(), nullable=False),
        sa.Column("genero", sa.String(length=100), nullable=False),
        sa.Column("sinopse", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("filmes")
