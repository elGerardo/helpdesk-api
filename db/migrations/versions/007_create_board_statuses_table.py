"""create board_statuses table

Revision ID: 007
Revises: 006
Create Date: 2026-01-03 00:00:07

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '007'
down_revision: Union[str, Sequence[str], None] = '006'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create board_statuses table."""
    op.create_table(
        'board_statuses',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('tenant_id', sa.BigInteger(), nullable=False),
        sa.Column('board_id', sa.BigInteger(), nullable=False),
        sa.Column('label', sa.String(255), nullable=False),
        sa.Column('slug', sa.String(255), nullable=False),
        sa.Column('type', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('slug', name='board_statuses_slug_unique'),
        sa.ForeignKeyConstraint(['tenant_id'], ['tenants.id'], name='board_statuses_tenant_id_foreign')
    )
    
    # Add comment for type column
    op.execute("COMMENT ON COLUMN board_statuses.type IS 'DEFAULT | CUSTOM'")


def downgrade() -> None:
    """Drop board_statuses table."""
    op.drop_table('board_statuses')
