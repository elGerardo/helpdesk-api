"""add status to tickets

Revision ID: 014
Revises: 013
Create Date: 2026-01-18 00:00:14

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '014'
down_revision: Union[str, Sequence[str], None] = '013'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add status column to tickets table."""
    op.add_column(
        'tickets',
        sa.Column('status', sa.String(255), nullable=True)
    )
    
    op.create_foreign_key(
        'tickets_status_foreign',
        'tickets',
        'board_statuses',
        ['status'],
        ['slug']
    )


def downgrade() -> None:
    """Remove status column from tickets table."""
    op.drop_constraint('tickets_status_foreign', 'tickets', type_='foreignkey')
    op.drop_column('tickets', 'status')
