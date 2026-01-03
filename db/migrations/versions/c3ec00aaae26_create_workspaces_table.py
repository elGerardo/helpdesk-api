"""create workspaces table

Revision ID: c3ec00aaae26
Revises: e12d0b601779
Create Date: 2026-01-03 02:08:28.270073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3ec00aaae26'
down_revision: Union[str, Sequence[str], None] = 'e12d0b601779'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create workspaces table."""
    op.create_table(
        'workspaces',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.String(255), nullable=True),
        sa.Column('logo', sa.String(255), nullable=True),
        sa.Column('color', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    """Drop workspaces table."""
    op.drop_table('workspaces')
