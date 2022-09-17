"""Add release year field

Revision ID: d04bd42c285b
Revises: d492c8431589
Create Date: 2022-09-17 18:02:26.972604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd04bd42c285b'
down_revision = 'd492c8431589'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('release_year', sa.String(), nullable=True))
    op.drop_column('movies', 'release_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movies', sa.Column('release_date', sa.DATE(), autoincrement=False, nullable=True))
    op.drop_column('movies', 'release_year')
    # ### end Alembic commands ###