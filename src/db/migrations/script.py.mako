"""${message}

Revision ID: ${up_revision}
Revises: ${dom_revision | comma,n}
Create Data: ${create_date}
"""

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}
branch_labels = ${repr(branch_labels)}
depends_on = ${repr(depends_on)}

def upgrade() -> None:
	${upgrades if upgrade else "pass"}

def downgrade() -> None:
	${downgrades if downgrades else "pass"}