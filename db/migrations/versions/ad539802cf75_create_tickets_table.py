"""create tickets table

Revision ID: ad539802cf75
Revises: 950c02b662bc
Create Date: 2026-01-03 02:08:58.235331

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad539802cf75'
down_revision: Union[str, Sequence[str], None] = '950c02b662bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create tickets table."""
    op.create_table(
        'tickets',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.Column('form_id', sa.BigInteger(), nullable=False),
        sa.Column('requester_name', sa.String(255), nullable=False),
        sa.Column('requester_mail', sa.String(255), nullable=True),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id']),
        sa.ForeignKeyConstraint(['board_id'], ['boards.id']),
        sa.ForeignKeyConstraint(['form_id'], ['forms.id'])
    )


def downgrade() -> None:
    """Drop tickets table."""
    op.drop_table('tickets')
