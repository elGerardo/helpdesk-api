"""add tenant foreign keys

Revision ID: 012
Revises: 011
Create Date: 2026-01-03 00:00:12

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '012'
down_revision: Union[str, Sequence[str], None] = '011'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Add users tenant foreign key constraint."""
    # Add users tenant foreign key
    op.create_foreign_key(
        'users_tenant_id_foreign',
        'users', 'tenants',
        ['tenant_id'], ['id']
    )


def downgrade() -> None:
    """Drop users tenant foreign key constraint."""
    op.drop_constraint('users_tenant_id_foreign', 'users', type_='foreignkey')
