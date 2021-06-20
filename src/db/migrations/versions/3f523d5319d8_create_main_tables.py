"""create_main_tables

Revision ID: 3f523d5319d8
Revises: 
Create Date: 2021-06-19 22:00:26.776136

"""
from sqlalchemy.sql.expression import true
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '3f523d5319d8'
down_revision = None
branch_labels = None
depends_on = None

def create_filmes_table() -> None:
    op.create_table(
        "filmes",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("tittle", sa.Text, nullable=False, index=True),
    )
def upgrade() -> None:
    create_filmes_table()


def downgrade() -> None:
    op.drop_table("filmes")
