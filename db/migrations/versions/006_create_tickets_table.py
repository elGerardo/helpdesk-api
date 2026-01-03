"""create tickets table

Revision ID: 006
Revises: 005
Create Date: 2026-01-03 00:00:06

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '006'
down_revision: Union[str, Sequence[str], None] = '005'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create tickets table."""
    op.create_table(
        'tickets',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.Column('form_id', sa.BigInteger(), nullable=False),
        sa.Column('requester_name', sa.String(255), nullable=False),
        sa.Column('requester_mail', sa.String(255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='tickets_tenant_id_foreign'),
        sa.ForeignKeyConstraint(['form_id'], ['forms.id'], name='tickets_form_id_foreign')
    )


def downgrade() -> None:
    """Drop tickets table."""
    op.drop_table('tickets')
