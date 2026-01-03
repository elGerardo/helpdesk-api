"""create junction tables

Revision ID: f1ced099f699
Revises: 634eac1022e6
Create Date: 2026-01-03 02:09:00.176852

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f1ced099f699'
down_revision: Union[str, Sequence[str], None] = '634eac1022e6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create junction tables."""
    # users_workspaces junction table
    op.create_table(
        'users_workspaces',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'workspace_id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id'])
    )
    
    # users_boards junction table
    op.create_table(
        'users_boards',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'workspace_id', 'board_id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id']),
        sa.ForeignKeyConstraint(['board_id'], ['boards.id'])
    )
    
    # ticket_responsibles junction table
    op.create_table(
        'ticket_responsibles',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('ticket_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'ticket_id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id']),
        sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'])
    )


def downgrade() -> None:
    """Drop junction tables."""
    op.drop_table('ticket_responsibles')
    op.drop_table('users_boards')
    op.drop_table('users_workspaces')
