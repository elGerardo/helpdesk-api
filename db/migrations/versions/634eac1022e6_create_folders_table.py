"""create folders table

Revision ID: 634eac1022e6
Revises: 6a4d96e74c7f
Create Date: 2026-01-03 02:08:59.818625

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '634eac1022e6'
down_revision: Union[str, Sequence[str], None] = '6a4d96e74c7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create folders table."""
    op.create_table(
        'folders',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('workspace_id', sa.BigInteger(), nullable=False),
        sa.Column('folder_id', sa.BigInteger(), nullable=True),
        sa.Column('folder_name', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['workspace_id'], ['workspaces.id']),
        sa.ForeignKeyConstraint(['folder_id'], ['folders.id'])
    )


def downgrade() -> None:
    """Drop folders table."""
    op.drop_table('folders')
