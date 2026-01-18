"""create notifications table

Revision ID: 013
Revises: 012
Create Date: 2026-01-18 00:00:13

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON


# revision identifiers, used by Alembic.
revision: str = '013'
down_revision: Union[str, Sequence[str], None] = '012'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create notifications table."""
    op.create_table(
        'notifications',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('row', sa.BigInteger(), nullable=False),
        sa.Column('table', sa.String(255), nullable=False),
        sa.Column('generated_by', sa.BigInteger(), nullable=False),
        sa.Column('deliveried_to', sa.BigInteger(), nullable=False),
        sa.Column('meta', JSON, nullable=True),
        sa.Column('is_seen', sa.Boolean(), server_default='false', nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('updated_at', sa.TIMESTAMP(), nullable=True),
        sa.Column('deleted_at', sa.TIMESTAMP(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['generated_by'], ['users.id'], name='notifications_generated_by_foreign'),
        sa.ForeignKeyConstraint(['deliveried_to'], ['users.id'], name='notifications_deliveried_to_foreign')
    )


def downgrade() -> None:
    """Drop notifications table."""
    op.drop_table('notifications')
