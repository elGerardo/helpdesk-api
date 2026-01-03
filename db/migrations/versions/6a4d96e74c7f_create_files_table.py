"""create files table

Revision ID: 6a4d96e74c7f
Revises: 608f030f0185
Create Date: 2026-01-03 02:08:59.377531

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6a4d96e74c7f'
down_revision: Union[str, Sequence[str], None] = '608f030f0185'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create files table."""
    op.create_table(
        'files',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('table', sa.String(255), nullable=False),
        sa.Column('row', sa.BigInteger(), nullable=False),
        sa.Column('file_name', sa.String(255), nullable=False),
        sa.Column('file_size', sa.String(255), nullable=False),
        sa.Column('path', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Drop files table."""
    op.drop_table('files')
