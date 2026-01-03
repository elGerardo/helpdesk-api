"""create board_statuses table

Revision ID: bd50cd8baafe
Revises: ad539802cf75
Create Date: 2026-01-03 02:08:58.601121

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd50cd8baafe'
down_revision: Union[str, Sequence[str], None] = 'ad539802cf75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create board_statuses table."""
    op.create_table(
        'board_statuses',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.Column('label', sa.String(255), nullable=False),
        sa.Column('slug', sa.String(255), nullable=False),
        sa.Column('type', sa.String(255), nullable=False, comment='DEFAULT | CUSTOM'),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug', name='board_statuses_slug_unique'),
        sa.ForeignKeyConstraint(['board_id'], ['boards.id'])
    )


def downgrade() -> None:
    """Drop board_statuses table."""
    op.drop_table('board_statuses')
