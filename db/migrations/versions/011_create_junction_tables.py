"""create junction tables

Revision ID: 011
Revises: 010
Create Date: 2026-01-03 00:00:11

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '011'
down_revision: Union[str, Sequence[str], None] = '010'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create junction tables."""
    
    # users_workspaces
    op.create_table(
        'users_workspaces',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'workspace_id', 'tenant_id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='users_workspaces_user_id_foreign')
    )
    
    # users_boards
    op.create_table(
        'users_boards',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'workspace_id', 'board_id', 'tenant_id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='users_boards_user_id_foreign')
    )
    
    # ticket_responsibles
    op.create_table(
        'ticket_responsibles',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('ticket_id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'ticket_id', 'tenant_id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='ticket_responsibles_user_id_foreign')
    )


def downgrade() -> None:
    """Drop junction tables."""
    op.drop_table('ticket_responsibles')
    op.drop_table('users_boards')
    op.drop_table('users_workspaces')
